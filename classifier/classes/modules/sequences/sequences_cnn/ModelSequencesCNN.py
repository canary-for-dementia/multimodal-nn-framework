from classifier.classes.core.Model import Model

from classifier.classes.modules.sequences.sequences_cnn.SequencesCNN import SequencesCNN


class ModelSequencesCNN(Model):

    def __init__(self, network_params: dict):
        super().__init__(device=network_params["device"])
        self._network = SequencesCNN(network_params).float().to(self._device)