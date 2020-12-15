from Topic import Topic

def generate_topics():
    m  = Topic(n_topics=15)
    m.read_document()
    docs = m.get_doc_set()
    m.nmf()
    m.generate_topics()
    m.print_topic_terms_weight()


if __name__ == "__main__":
    generate_topics()
