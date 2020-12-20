from NMFModel import NMFModel

def generate_topics():
    
    solver = ["mu", "cd"]
    beta_loss = ["kullback-leibler", "frobenius"]

    for s in solver:
        for b in beta_loss:
            nmf = NMFModel(n_topics=15, s=s, b=b)
            nmf.read_document()
            nmf.generate_topics()

if __name__ == "__main__":
    generate_topics()
