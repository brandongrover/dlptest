import socketserver
import sys
from datetime import datetime

DNS_HEADER_LENGTH = 12
IP = '192.168.155.155'


class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        socket = self.request[1]
        data = self.request[0].strip()

        if len(data) < DNS_HEADER_LENGTH:
            return

        try:
            all_questions = self.dns_extract_questions(data)
        except IndexError:
            return

        accepted_questions = []
        for question in all_questions:
            name = str(b'.'.join(question['name']), encoding='UTF-8')
            if question['qtype'] == b'\x00\x01' and question['qclass'] == b'\x00\x01':
                accepted_questions.append(question)
                print('\033[32m{}\033[39m'.format(name))
                with open(f"dns_requests-{datetime.today().strftime('%Y-%m-%d')}.txt", "a") as file:
                    file.write(f"{self.client_address[0]}|{name}\n")
        response = self.dns_response_header(data) + self.dns_response_questions(accepted_questions) + self.dns_response_answers(accepted_questions)
        socket.sendto(response, self.client_address)

    def dns_extract_questions(self, data):
        questions = []
        n = (data[4] << 8) + data[5]
        pointer = DNS_HEADER_LENGTH
        for _ in range(n):
            question = {
                'name': [],
                'qtype': '',
                'qclass': '',
            }
            length = data[pointer]
            while length != 0:
                start = pointer + 1
                end = pointer + length + 1
                question['name'].append(data[start:end])
                pointer += length + 1
                length = data[pointer]
            question['qtype'] = data[pointer+1:pointer+3]
            question['qclass'] = data[pointer+3:pointer+5]
            pointer += 5
            questions.append(question)
        return questions

    def dns_response_header(self, data):
        header = b''
        header += data[:2]
        header += b'\x80\x00'
        header += data[4:6]
        header += data[4:6]
        header += b'\x00\x00'
        header += b'\x00\x00'
        return header

    def dns_response_questions(self, questions):
        sections = b''
        for question in questions:
            section = b''
            for label in question['name']:
                section += bytes([len(label)])
                section += label
            section += b'\x00'
            section += question['qtype']
            section += question['qclass']
            sections += section
        return sections

    def dns_response_answers(self, questions):
        records = b''
        for question in questions:
            record = b''
            for label in question['name']:
                record += bytes([len(label)])
                record += label
            record += b'\x00'
            record += question['qtype']
            record += question['qclass']
            record += b'\x00\x00\x00\x00'
            record += b'\x00\x04'
            record += b''.join(map(lambda x: bytes([int(x)]), IP.split('.')))
            records += record
        return records


if __name__ == '__main__':
    port = int(sys.argv) if len(sys.argv) > 1 else 53
    host, port = '', int(port)
    server = socketserver.ThreadingUDPServer((host, port), DNSHandler)
    print('\033[36mStarted DNS server.\033[39m')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        sys.exit(0)