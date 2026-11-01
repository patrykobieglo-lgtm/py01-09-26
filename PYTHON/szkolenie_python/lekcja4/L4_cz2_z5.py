zapisy = ["ola@wp.pl", "jan@onet.pl", "ola@wp.pl",
          "ewa@gmail.com", "jan@onet.pl", "ola@wp.pl"]
print(len(zapisy))
unikalne = set(zapisy)
posortowane = sorted(unikalne)
zapisy.count("ola@wp.pl")
print("Zapisów:", len(zapisy), "unikalnych:", len(unikalne))
print(posortowane)
print("ola@wp.pl:", zapisy.count("ola@wp.pl"), "razy")