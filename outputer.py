# -*- coding: utf-8 -*-
class Outputer(object):

    def __init__(self):
        self.result = []

    def collect_data(self, data):
        if data is None:
            return
        self.result.append(data)


    def output_html(self):
        fout = open('result.html', 'w')
        fout.write('<html><style>table{border_collapse: collapse;} table, td, tr{border: 1px solid black;}</style><body><table>')

        for data in self.result:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data.get('url', " "))
            fout.write('<td>%s</td>' % data.get('title', " ").encode('utf-8'))
            fout.write('<td>%s</td>' % data.get('p', " ").encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table></body><html>')