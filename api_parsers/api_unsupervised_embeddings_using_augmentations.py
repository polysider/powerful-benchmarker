from .base_api_parser import BaseAPIParser

class APIUnsupervisedEmbeddingsUsingAugmentations(BaseAPIParser):
    def get_trainer_kwargs(self):
        trainer_kwargs = super().get_trainer_kwargs()
        transforms = self.get_transforms()
        trainer_kwargs["transforms"] = [transforms[k] for k in transforms.keys() if k.startswith("augmentation")]
        trainer_kwargs["sampler"] = None
        trainer_kwargs["set_min_label_to_zero"] = False
        return trainer_kwargs