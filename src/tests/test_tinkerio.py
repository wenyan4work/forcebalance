from __future__ import absolute_import
import shutil
import forcebalance

from forcebalance.nifty import *
from .test_target import TargetTest # general targets tests defined in test_target.py

class TestInteraction_TINKER(TargetTest):

    def setup_method(self, method):
        super().setup_method(method)
        self.options.update({
                'penalty_additive': 0.01,
                'jobtype': 'NEWTON',
                'forcefield': ['cl4.prm'],
                'amoeba_pol': 'direct'})

        self.tgt_opt.update({'type':'Interaction_TINKER',
                             'name':'ccl4-h2o-1',
                             'energy_denom':1.0,
                             'attenuate':'True',
                             'fragment1':'1-5',
                             'fragment2':'6-8',
                             'energy-upper':20.0})

        self.ff = forcebalance.forcefield.FF(self.options)

        self.ffname = self.options['forcefield'][0][:-3]
        self.filetype = self.options['forcefield'][0][-3:]
        self.mvals = [.5]*self.ff.np

        if (which('testgrad') == ''):
            self.skipTest("TINKER programs are not in the PATH.")

        self.logger.debug("Setting up Interaction_TINKER target\n")
        self.target = forcebalance.tinkerio.Interaction_TINKER(self.options, self.tgt_opt, self.ff)

    def teardown_method(self):
        shutil.rmtree('temp')
        super().teardown_method()

    def shortDescription(self):
        """@override ForceBalanceTestCase.shortDescription()"""
        return super(TestInteraction_TINKER,self).shortDescription() + " (Interaction_TINKER)"
