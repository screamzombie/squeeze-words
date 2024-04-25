from calculate import *

if __name__ == '__main__':
    c = controller()
    c.load_paper()
    c.calculate_freq_dict()
    c.storage_all_content_words_freq()
    c.storage_words_freq_by_paper()
    c.create_paper_directory()
    c.storage_sections_words_freq()
