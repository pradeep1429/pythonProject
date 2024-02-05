
from abc import ABC, abstractmethod


class IMince(ABC):

    @abstractmethod
    def mince(self, item):
        raise NotImplementedError


class IChopper(ABC):

    @abstractmethod
    def chop(self, item):
        raise NotImplementedError


class FoodProcessor(IMince, IChopper):

    def chop(self, item):
        # code logic to chop the items
        print(f"chopping the {item}")

    def mince(self, item):
        # code logic to mince the items
        print(f"Minicing the {item}")


# class Mincer(IMince):
#
#     def mince(self, item):
#         super().mince(item)
#
# class Chopper(IChopper):
#     def chop(self,item):
#         super().chop(item)


# client code
class Processor:

    def execute(self, fp: [IChopper], item):
        for each_mincer in fp:
            each_mincer.chop(item)

    def action(self, fp: [IMince], item):
        for each_chopper in fp:
            each_chopper.mince(item)


if __name__ == "__main__":
    fp_ins = FoodProcessor()
    prc_ins = Processor()
    prc_ins.execute([fp_ins], "onions")
    prc_ins.action([fp_ins], "carrots")