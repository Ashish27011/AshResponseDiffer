from banners import banner
from core import request_handler
from core import response_parser
from core import comparator
from core import body_diff
from core import analyzer
from core import reporter
from outputs import writeup

url_one, url_two  = request_handler.show_validator()
banner.s_banner()
url_one_dick, url_two_dick = response_parser.show_response(url_one, url_two )
comp_response_dick = comparator.show_comparator(url_one_dick, url_two_dick)
terminal_data, file_data = body_diff.show_diff(url_one_dick, url_two_dick)
summary_response = analyzer.show_analyzer(url_one_dick, url_two_dick)
reporter.show_reports(url_one_dick, url_two_dick, comp_response_dick, terminal_data, summary_response)
writeup.show_writeup(url_one_dick, url_two_dick, comp_response_dick, terminal_data, summary_response)
banner.e_banner()