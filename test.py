collections.Counter



 with tf.gfile.GFile("simple-examples/data/ptb.test.txt", "r") as f:
    return f.read().replace("\n", "<eos>").split()

