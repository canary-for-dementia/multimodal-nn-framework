from classifier.classes.core.Model import Model

from classifier.classes.modules.sequences.sequences_cnn_rnn.SequencesCNNRNN import SequencesCNNRNN


class ModelSequencesCNNRNN(Model):

    def __init__(self, network_params: dict):
        super().__init__(device=network_params["device"])
        self._network = SequencesCNNRNN(network_params).to(self._device)
