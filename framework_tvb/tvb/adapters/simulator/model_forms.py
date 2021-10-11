# -*- coding: utf-8 -*-
#
#
# TheVirtualBrain-Framework Package. This package holds all Data Management, and
# Web-UI helpful to run brain-simulations. To use it, you also need do download
# TheVirtualBrain-Scientific Package (for simulators). See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2022, Baycrest Centre for Geriatric Care ("Baycrest") and others
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#

from tvb.simulator import models
from tvb.adapters.simulator.form_with_ranges import FormWithRanges
from tvb.basic.neotraits.api import TupleEnum
from tvb.core.neotraits.forms import Form, ArrayField, MultiSelectField


class ModelsEnum(TupleEnum):
    GENERIC_2D_OSCILLATOR = (models.ModelsEnum.GENERIC_2D_OSCILLATOR.get_class(), "Generic 2D Oscillator")
    KURAMOTO = (models.ModelsEnum.KURAMOTO.get_class(), "Kuramoto Oscillator")
    SUP_HOPF = (models.ModelsEnum.SUP_HOPF.get_class(), "Suphopf")
    HOPFIELD = (models.ModelsEnum.HOPFIELD.get_class(), "Hopfield")
    EPILEPTOR = (models.ModelsEnum.EPILEPTOR.get_class(), "Epileptor")
    EPILEPTOR_2D = (models.ModelsEnum.EPILEPTOR_2D.get_class(), "Epileptor2D")
    EPILEPTOR_CODIM_3 = (models.ModelsEnum.EPILEPTOR_CODIM_3.get_class(), "Epileptor Codim 3")
    EPILEPTOR_CODIM_3_SLOW = (models.ModelsEnum.EPILEPTOR_CODIM_3_SLOW.get_class(), "Epileptor Codim 3 Ultra-Slow Modulations")
    EPILEPTOR_RS = (models.ModelsEnum.EPILEPTOR_RS.get_class(), "Epileptor Resting State")
    JANSEN_RIT = (models.ModelsEnum.JANSEN_RIT.get_class(), "Jansen-Rit")
    ZETTERBERG_JANSEN = (models.ModelsEnum.ZETTERBERG_JANSEN.get_class(), "Zetterberg-Jansen")
    REDUCED_WONG_WANG = (models.ModelsEnum.REDUCED_WONG_WANG.get_class(), "Reduced Wong-Wang")
    REDUCED_WONG_WANG_EXCH_INH = (models.ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.get_class(), "Reduced Wong-Wang With Excitatory And Inhibitory Coupled Populations")
    REDUCED_SET_FITZ_HUGH_NAGUMO = (models.ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.get_class(), "Stefanescu-Jirsa 2D")
    REDUCED_SET_HINDMARSH_ROSE = (models.ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.get_class(), "Stefanescu-Jirsa 3D")
    ZERLAUT_FIRST_ORDER = (models.ModelsEnum.ZERLAUT_FIRST_ORDER.get_class(), "Zerlaut Adaptation First Order")
    ZERLAUT_SECOND_ORDER = (models.ModelsEnum.ZERLAUT_SECOND_ORDER.get_class(), "Zerlaut Adaptation Second Order")
    MONTBRIO_PAZO_ROXIN = (models.ModelsEnum.MONTBRIO_PAZO_ROXIN.get_class(), "Montbrio Pazo Roxin")
    COOMBES_BYRNE = (models.ModelsEnum.COOMBES_BYRNE.get_class(), "Coombes Byrne")
    COOMBES_BYRNE_2D = (models.ModelsEnum.COOMBES_BYRNE_2D.get_class(), "Coombes Byrne 2D")
    GAST_SCHMIDT_KNOSCHE_SD = (models.ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.get_class(), "Gast Schmidt Knosche_Sd")
    GAST_SCHMIDT_KNOSCHE_SF = (models.ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.get_class(), "Gast Schmidt Knosche_Sf")
    DUMONT_GUTKIN = (models.ModelsEnum.DUMONT_GUTKIN.get_class(), "Dumont Gutkin")
    LINEAR = (models.ModelsEnum.LINEAR.get_class(), "Linear Model")
    WILSON_COWAN = (models.ModelsEnum.WILSON_COWAN.get_class(), "Wilson-Cowan")
    LARTER_BREAKSPEAR = (models.ModelsEnum.LARTER_BREAKSPEAR.get_class(), "Larter-Breakspear")


def get_model_to_form_dict():
    model_class_to_form = {
        ModelsEnum.GENERIC_2D_OSCILLATOR.value: Generic2dOscillatorModelForm,
        ModelsEnum.KURAMOTO.value: KuramotoModelForm,
        ModelsEnum.SUP_HOPF.value: SupHopfModelForm,
        ModelsEnum.HOPFIELD.value: HopfieldModelForm,
        ModelsEnum.EPILEPTOR.value: EpileptorModelForm,
        ModelsEnum.EPILEPTOR_2D.value: Epileptor2DModelForm,
        ModelsEnum.EPILEPTOR_CODIM_3.value: EpileptorCodim3ModelForm,
        ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value: EpileptorCodim3SlowModModelForm,
        ModelsEnum.EPILEPTOR_RS.value: EpileptorRestingStateModelForm,
        ModelsEnum.JANSEN_RIT.value: JansenRitModelForm,
        ModelsEnum.ZETTERBERG_JANSEN.value: ZetterbergJansenModelForm,
        ModelsEnum.REDUCED_WONG_WANG.value: ReducedWongWangModelForm,
        ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value: ReducedWongWangExcInhModelForm,
        ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value: ReducedSetFitzHughNagumoModelForm,
        ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value: ReducedSetHindmarshRoseModelForm,
        ModelsEnum.ZERLAUT_FIRST_ORDER.value: ZerlautAdaptationFirstOrderModelForm,
        ModelsEnum.ZERLAUT_SECOND_ORDER.value: ZerlautAdaptationSecondOrderModelForm,
        ModelsEnum.MONTBRIO_PAZO_ROXIN.value: MontbrioPazoRoxinModelForm,
        ModelsEnum.COOMBES_BYRNE.value: CoombesByrneModelForm,
        ModelsEnum.COOMBES_BYRNE_2D.value: CoombesByrne2DModelForm,
        ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value: GastSchmidtKnoscheSDModelForm,
        ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value: GastSchmidtKnoscheSFModelForm,
        ModelsEnum.DUMONT_GUTKIN.value: DumontGutkinModelForm,
        ModelsEnum.LINEAR.value: LinearModelForm,
        ModelsEnum.WILSON_COWAN.value: WilsonCowanModelForm,
        ModelsEnum.LARTER_BREAKSPEAR.value: LarterBreakspearModelForm
    }

    return model_class_to_form


def get_form_for_model(model_class):
    return get_model_to_form_dict().get(model_class)


class StateVariableRangesForm(Form):

    def __init__(self):
        super(StateVariableRangesForm, self).__init__()


class ModelForm(FormWithRanges):

    def __init__(self, are_voi_disabled=False):
        super(ModelForm, self).__init__()
        self.are_voi_disabled = are_voi_disabled

    def fill_from_trait(self, trait):
        # type: (Model) -> None
        super(ModelForm, self).fill_from_trait(trait)

        if self.are_voi_disabled:
            self.variables_of_interest.disabled = True


class Generic2dOscillatorModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(Generic2dOscillatorModelForm, self).__init__(are_voi_disabled)
        self.tau = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.tau)
        self.I = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.I)
        self.a = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.a)
        self.b = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.b)
        self.c = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.c)
        self.d = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.d)
        self.e = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.e)
        self.f = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.f)
        self.g = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.g)
        self.alpha = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.alpha)
        self.beta = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.beta)
        self.gamma = ArrayField(ModelsEnum.GENERIC_2D_OSCILLATOR.value.gamma)
        self.variables_of_interest = MultiSelectField(
            ModelsEnum.GENERIC_2D_OSCILLATOR.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"tau": r":math:`\tau`", "a": ":math:`a`", "b": ":math:`b`", "c": ":math:`c`", "I": ":math:`I`",
                "d": ":math:`d`", "e": ":math:`e`", "f": ":math:`f`", "g": ":math:`g`", "alpha": r":math:`\alpha`",
                "beta": r":math:`\beta`", "gamma": r":math:`\gamma`"}


class KuramotoModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(KuramotoModelForm, self).__init__(are_voi_disabled)
        self.omega = ArrayField(ModelsEnum.KURAMOTO.value.omega)
        self.variables_of_interest = MultiSelectField(ModelsEnum.KURAMOTO.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"omega": r":math:`\omega`"}


class SupHopfModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(SupHopfModelForm, self).__init__(are_voi_disabled)
        self.a = ArrayField(ModelsEnum.SUP_HOPF.value.a)
        self.omega = ArrayField(ModelsEnum.SUP_HOPF.value.omega)
        self.variables_of_interest = MultiSelectField(ModelsEnum.SUP_HOPF.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"a": ":math:`a`", "omega": r":math:`\omega`"}


class HopfieldModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(HopfieldModelForm, self).__init__(are_voi_disabled)
        self.taux = ArrayField(ModelsEnum.HOPFIELD.value.taux)
        self.tauT = ArrayField(ModelsEnum.HOPFIELD.value.tauT)
        self.dynamic = ArrayField(ModelsEnum.HOPFIELD.value.dynamic)
        self.variables_of_interest = MultiSelectField(ModelsEnum.HOPFIELD.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"taux": r":math:`\tau_{x}`", "tauT": r":math:`\tau_{\theta}`", "dynamic": "Dynamic"}


class EpileptorModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(EpileptorModelForm, self).__init__(are_voi_disabled)
        self.a = ArrayField(ModelsEnum.EPILEPTOR.value.a)
        self.b = ArrayField(ModelsEnum.EPILEPTOR.value.b)
        self.c = ArrayField(ModelsEnum.EPILEPTOR.value.c)
        self.d = ArrayField(ModelsEnum.EPILEPTOR.value.d)
        self.r = ArrayField(ModelsEnum.EPILEPTOR.value.r)
        self.s = ArrayField(ModelsEnum.EPILEPTOR.value.s)
        self.x0 = ArrayField(ModelsEnum.EPILEPTOR.value.x0)
        self.Iext = ArrayField(ModelsEnum.EPILEPTOR.value.Iext)
        self.slope = ArrayField(ModelsEnum.EPILEPTOR.value.slope)
        self.Iext2 = ArrayField(ModelsEnum.EPILEPTOR.value.Iext2)
        self.tau = ArrayField(ModelsEnum.EPILEPTOR.value.tau)
        self.aa = ArrayField(ModelsEnum.EPILEPTOR.value.aa)
        self.bb = ArrayField(ModelsEnum.EPILEPTOR.value.bb)
        self.Kvf = ArrayField(ModelsEnum.EPILEPTOR.value.Kvf)
        self.Kf = ArrayField(ModelsEnum.EPILEPTOR.value.Kf)
        self.Ks = ArrayField(ModelsEnum.EPILEPTOR.value.Ks)
        self.tt = ArrayField(ModelsEnum.EPILEPTOR.value.tt)
        self.modification = ArrayField(ModelsEnum.EPILEPTOR.value.modification)
        self.variables_of_interest = MultiSelectField(ModelsEnum.EPILEPTOR.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"Iext": ":math:`I_{ext}`", "Iext2": ":math:`I_{ext2}`", "r": ":math:`r`", "x0": ":math:`x_0`",
                "slope": ":math:`slope`"}


class Epileptor2DModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(Epileptor2DModelForm, self).__init__(are_voi_disabled)
        self.a = ArrayField(ModelsEnum.EPILEPTOR_2D.value.a)
        self.b = ArrayField(ModelsEnum.EPILEPTOR_2D.value.b)
        self.c = ArrayField(ModelsEnum.EPILEPTOR_2D.value.c)
        self.d = ArrayField(ModelsEnum.EPILEPTOR_2D.value.d)
        self.r = ArrayField(ModelsEnum.EPILEPTOR_2D.value.r)
        self.x0 = ArrayField(ModelsEnum.EPILEPTOR_2D.value.x0)
        self.Iext = ArrayField(ModelsEnum.EPILEPTOR_2D.value.Iext)
        self.slope = ArrayField(ModelsEnum.EPILEPTOR_2D.value.slope)
        self.Kvf = ArrayField(ModelsEnum.EPILEPTOR_2D.value.Kvf)
        self.Ks = ArrayField(ModelsEnum.EPILEPTOR_2D.value.Ks)
        self.tt = ArrayField(ModelsEnum.EPILEPTOR_2D.value.tt)
        self.modification = ArrayField(ModelsEnum.EPILEPTOR_2D.value.modification)
        self.variables_of_interest = MultiSelectField(ModelsEnum.EPILEPTOR_2D.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"r": ":math:`r`", "Iext": ":math:`I_{ext}`", "x0": ":math:`x_0`"}


class EpileptorCodim3ModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(EpileptorCodim3ModelForm, self).__init__(are_voi_disabled)
        self.mu1_start = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.mu1_start)
        self.mu2_start = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.mu2_start)
        self.nu_start = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.nu_start)
        self.mu1_stop = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.mu1_stop)
        self.mu2_stop = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.mu2_stop)
        self.nu_stop = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.nu_stop)
        self.b = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.b)
        self.R = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.R)
        self.c = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.c)
        self.dstar = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.dstar)
        self.Ks = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.Ks)
        self.N = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.N)
        self.modification = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3.value.modification)
        self.variables_of_interest = MultiSelectField(ModelsEnum.EPILEPTOR_CODIM_3.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"mu1_start": ":math:`mu_1 start`", "mu2_start": ":math:`mu_2 start`", "nu_start": ":math:`nu start`",
                "mu1_stop": ":math:`mu_1 stop`", "mu2_stop": ":math:`mu_2 stop`", "nu_stop": ":math:`nu stop`",
                "b": ":math:`b`", "R": ":math:`R`", "c": ":math:`c`", "dstar": ":math:`d^*`", "N": ":math:`N`",
                "Ks": ":math:`K_s`"}


class EpileptorCodim3SlowModModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(EpileptorCodim3SlowModModelForm, self).__init__(are_voi_disabled)
        self.mu1_Ain = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.mu1_Ain)
        self.mu2_Ain = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.mu2_Ain)
        self.nu_Ain = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.nu_Ain)
        self.mu1_Bin = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.mu1_Bin)
        self.mu2_Bin = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.mu2_Bin)
        self.nu_Bin = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.nu_Bin)
        self.mu1_Aend = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.mu1_Aend)
        self.mu2_Aend = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.mu2_Aend)
        self.nu_Aend = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.nu_Aend)
        self.mu1_Bend = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.mu1_Bend)
        self.mu2_Bend = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.mu2_Bend)
        self.nu_Bend = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.nu_Bend)
        self.b = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.b)
        self.R = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.R)
        self.c = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.c)
        self.cA = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.cA)
        self.cB = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.cB)
        self.dstar = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.dstar)
        self.Ks = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.Ks)
        self.N = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.N)
        self.modification = ArrayField(ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.modification)
        self.variables_of_interest = MultiSelectField(
            ModelsEnum.EPILEPTOR_CODIM_3_SLOW.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"mu1_Ain": "mu1_Ain", "mu2_Ain": "mu2_Ain", "nu_Ain": "nu_Ain", "mu1_Bin": "mu1_Bin",
                "mu2_Bin": "mu2_Bin", "nu_Bin": "nu_Bin", "mu1_Aend": "mu1_Aend", "mu2_Aend": "mu2_Aend",
                "nu_Aend":  "nu_Aend", "mu1_Bend": "mu1_Bend", "mu2_Bend": "mu2_Bend", "nu_Bend": "nu_Bend", "b": "b",
                "R": "R", "c": "c", "dstar": "dstar", "N": "N"}


class EpileptorRestingStateModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(EpileptorRestingStateModelForm, self).__init__(are_voi_disabled)
        self.a = ArrayField(ModelsEnum.EPILEPTOR_RS.value.a)
        self.b = ArrayField(ModelsEnum.EPILEPTOR_RS.value.b)
        self.c = ArrayField(ModelsEnum.EPILEPTOR_RS.value.c)
        self.d = ArrayField(ModelsEnum.EPILEPTOR_RS.value.d)
        self.r = ArrayField(ModelsEnum.EPILEPTOR_RS.value.r)
        self.s = ArrayField(ModelsEnum.EPILEPTOR_RS.value.s)
        self.x0 = ArrayField(ModelsEnum.EPILEPTOR_RS.value.x0)
        self.Iext = ArrayField(ModelsEnum.EPILEPTOR_RS.value.Iext)
        self.slope = ArrayField(ModelsEnum.EPILEPTOR_RS.value.slope)
        self.Iext2 = ArrayField(ModelsEnum.EPILEPTOR_RS.value.Iext2)
        self.tau = ArrayField(ModelsEnum.EPILEPTOR_RS.value.tau)
        self.aa = ArrayField(ModelsEnum.EPILEPTOR_RS.value.aa)
        self.bb = ArrayField(ModelsEnum.EPILEPTOR_RS.value.bb)
        self.Kvf = ArrayField(ModelsEnum.EPILEPTOR_RS.value.Kvf)
        self.Kf = ArrayField(ModelsEnum.EPILEPTOR_RS.value.Kf)
        self.Ks = ArrayField(ModelsEnum.EPILEPTOR_RS.value.Ks)
        self.tt = ArrayField(ModelsEnum.EPILEPTOR_RS.value.tt)
        self.tau_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.tau_rs)
        self.I_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.I_rs)
        self.a_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.a_rs)
        self.b_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.b_rs)
        self.d_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.d_rs)
        self.e_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.e_rs)
        self.f_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.f_rs)
        self.alpha_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.alpha_rs)
        self.beta_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.beta_rs)
        self.K_rs = ArrayField(ModelsEnum.EPILEPTOR_RS.value.K_rs)
        self.p = ArrayField(ModelsEnum.EPILEPTOR_RS.value.p)
        self.variables_of_interest = MultiSelectField(ModelsEnum.EPILEPTOR_RS.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"Iext": ":math:`I_{ext}`", "Iext2": ":math:`I_{ext2}`", "r": ":math:`r`", "x0": ":math:`x_0`",
                "slope": ":math:`slope`", "tau_rs": r":math:`\tau_{rs}`", "a_rs": ":math:`a_{rs}`",
                "b_rs": ":math:`b_{rs}`", "I_rs": ":math:`I_{rs}`", "d_rs": ":math:`d_{rs}`",
                "e_rs": ":math:`e_{rs}`", "f_rs": ":math:`f_{rs}`", "alpha_rs": r":math:`\alpha_{rs}`",
                "beta_rs": r":math:`\beta_{rs}`", "gamma_rs": r":math:`\gamma_{rs}`"}


class JansenRitModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(JansenRitModelForm, self).__init__(are_voi_disabled)
        self.A = ArrayField(ModelsEnum.JANSEN_RIT.value.A)
        self.B = ArrayField(ModelsEnum.JANSEN_RIT.value.B)
        self.a = ArrayField(ModelsEnum.JANSEN_RIT.value.a)
        self.b = ArrayField(ModelsEnum.JANSEN_RIT.value.b)
        self.v0 = ArrayField(ModelsEnum.JANSEN_RIT.value.v0)
        self.nu_max = ArrayField(ModelsEnum.JANSEN_RIT.value.nu_max)
        self.r = ArrayField(ModelsEnum.JANSEN_RIT.value.r)
        self.J = ArrayField(ModelsEnum.JANSEN_RIT.value.J)
        self.a_1 = ArrayField(ModelsEnum.JANSEN_RIT.value.a_1)
        self.a_2 = ArrayField(ModelsEnum.JANSEN_RIT.value.a_2)
        self.a_3 = ArrayField(ModelsEnum.JANSEN_RIT.value.a_3)
        self.a_4 = ArrayField(ModelsEnum.JANSEN_RIT.value.a_4)
        self.p_min = ArrayField(ModelsEnum.JANSEN_RIT.value.p_min)
        self.p_max = ArrayField(ModelsEnum.JANSEN_RIT.value.p_max)
        self.mu = ArrayField(ModelsEnum.JANSEN_RIT.value.mu)
        self.variables_of_interest = MultiSelectField(ModelsEnum.JANSEN_RIT.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"A": ":math:`A`", "B": ":math:`B`", "a": ":math:`a`", "b": ":math:`b`", "v0": ":math:`v_0`",
                "nu_max": r":math:`\nu_{max}`", "r": ":math:`r`", "J": ":math:`J`", "a_1": r":math:`\alpha_1`",
                "a_2": r":math:`\alpha_2`", "a_3": r":math:`\alpha_3`", "a_4": r":math:`\alpha_4`",
                "p_min": ":math:`p_{min}`", "p_max": ":math:`p_{max}`", "mu": r":math:`\mu_{max}`"}


class ZetterbergJansenModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(ZetterbergJansenModelForm, self).__init__(are_voi_disabled)
        self.He = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.He)
        self.Hi = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.Hi)
        self.ke = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.ke)
        self.ki = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.ki)
        self.e0 = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.e0)
        self.rho_2 = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.rho_2)
        self.rho_1 = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.rho_1)
        self.gamma_1 = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.gamma_1)
        self.gamma_2 = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.gamma_2)
        self.gamma_3 = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.gamma_3)
        self.gamma_4 = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.gamma_4)
        self.gamma_5 = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.gamma_5)
        self.gamma_1T = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.gamma_1T)
        self.gamma_2T = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.gamma_2T)
        self.gamma_3T = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.gamma_3T)
        self.P = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.P)
        self.U = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.U)
        self.Q = ArrayField(ModelsEnum.ZETTERBERG_JANSEN.value.Q)
        self.variables_of_interest = MultiSelectField(ModelsEnum.ZETTERBERG_JANSEN.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"He": ":math:`H_e`", "Hi": ":math:`H_i`", "ke": r":math:`\kappa_e`", "ki": r":math:`\kappa_i`",
                "e0": r":math:`e_0`", "rho_2": r":math:`\rho_2`", "rho_1": r":math:`\rho_1`",
                "gamma_1": r":math:`\gamma_1`", "gamma_2": r":math:`\gamma_2`", "gamma_3": r":math:`\gamma_3`",
                "gamma_4": r":math:`\gamma_4`", "gamma_5": r":math:`\gamma_5`", "P": ":math:`P`", "U": ":math:`U`",
                "Q": ":math:`Q`"}


class ReducedWongWangModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(ReducedWongWangModelForm, self).__init__(are_voi_disabled)
        self.a = ArrayField(ModelsEnum.REDUCED_WONG_WANG.value.a)
        self.b = ArrayField(ModelsEnum.REDUCED_WONG_WANG.value.b)
        self.d = ArrayField(ModelsEnum.REDUCED_WONG_WANG.value.d)
        self.gamma = ArrayField(ModelsEnum.REDUCED_WONG_WANG.value.gamma)
        self.tau_s = ArrayField(ModelsEnum.REDUCED_WONG_WANG.value.tau_s)
        self.w = ArrayField(ModelsEnum.REDUCED_WONG_WANG.value.w)
        self.J_N = ArrayField(ModelsEnum.REDUCED_WONG_WANG.value.J_N)
        self.I_o = ArrayField(ModelsEnum.REDUCED_WONG_WANG.value.I_o)
        self.sigma_noise = ArrayField(ModelsEnum.REDUCED_WONG_WANG.value.sigma_noise)
        self.variables_of_interest = MultiSelectField(ModelsEnum.REDUCED_WONG_WANG.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"a": ":math:`a`", "b": ":math:`b`", "d": ":math:`d`", "gamma": r":math:`\gamma`",
                "tau_s":  r":math:`\tau_S`", "w": r":math:`w`", "J_N": r":math:`J_{N}`", "I_o": ":math:`I_{o}`"}


class ReducedWongWangExcInhModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(ReducedWongWangExcInhModelForm, self).__init__(are_voi_disabled)
        self.a_e = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.a_e)
        self.b_e = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.b_e)
        self.d_e = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.d_e)
        self.gamma_e = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.gamma_e)
        self.tau_e = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.tau_e)
        self.w_p = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.w_p)
        self.J_N = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.J_N)
        self.W_e = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.W_e)
        self.a_i = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.a_i)
        self.b_i = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.b_i)
        self.d_i = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.d_i)
        self.gamma_i = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.gamma_i)
        self.tau_i = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.tau_i)
        self.J_i = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.J_i)
        self.W_i = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.W_i)
        self.I_o = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.I_o)
        self.G = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.G)
        self.lamda = ArrayField(ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.lamda)
        self.variables_of_interest = MultiSelectField(
            ModelsEnum.REDUCED_WONG_WANG_EXCH_INH.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"a_e": ":math:`a_e`", "b_e": ":math:`b_e`", "d_e": ":math:`d_e`", "gamma_e": r":math:`\gamma_e`",
                "tau_e": r":math:`\tau_e`", "W_e": r":math:`W_e`", "w_p": r":math:`w_p`", "J_N": r":math:`J_N`",
                "a_i": ":math:`a_i`", "b_i": ":math:`b_i`", "d_i": ":math:`d_i`", "gamma_i": r":math:`\gamma_i`",
                "tau_i": r":math:`\tau_i`", "W_i": r":math:`W_i`", "J_i": r":math:`J_{i}`", "I_o": ":math:`I_{o}`",
                "G": ":math:`G`", "lamda": r":math:`\lambda`"}


class ReducedSetFitzHughNagumoModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(ReducedSetFitzHughNagumoModelForm, self).__init__(are_voi_disabled)
        self.tau = ArrayField(ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value.tau)
        self.a = ArrayField(ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value.a)
        self.b = ArrayField(ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value.b)
        self.K11 = ArrayField(ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value.K11)
        self.K12 = ArrayField(ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value.K12)
        self.K21 = ArrayField(ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value.K21)
        self.sigma = ArrayField(ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value.sigma)
        self.mu = ArrayField(ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value.mu)
        self.variables_of_interest = MultiSelectField(
            ModelsEnum.REDUCED_SET_FITZ_HUGH_NAGUMO.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"tau": r":math:`\tau`", "a": ":math:`a`", "b": ":math:`b`", "K11": ":math:`K_{11}`",
                "K12": ":math:`K_{12}`", "K21": ":math:`K_{21}`", "sigma": r":math:`\sigma`", "mu": r":math:`\mu`"}


class ReducedSetHindmarshRoseModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(ReducedSetHindmarshRoseModelForm, self).__init__(are_voi_disabled)
        self.r = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.r)
        self.a = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.a)
        self.b = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.b)
        self.c = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.c)
        self.d = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.d)
        self.s = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.s)
        self.xo = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.xo)
        self.K11 = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.K11)
        self.K12 = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.K12)
        self.K21 = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.K21)
        self.sigma = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.sigma)
        self.mu = ArrayField(ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.mu)
        self.variables_of_interest = MultiSelectField(
            ModelsEnum.REDUCED_SET_HINDMARSH_ROSE.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"r": ":math:`r`", "a": ":math:`a`", "b": ":math:`b`", "c": ":math:`c`", "d": ":math:`d`",
                "s": ":math:`s`", "xo": ":math:`x_{o}`", "K11": ":math:`K_{11}`", "K12": ":math:`K_{12}`",
                "K21": ":math:`K_{21}`", "sigma": r":math:`\sigma`", "mu": r":math:`\mu`"}


class ZerlautAdaptationFirstOrderModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(ZerlautAdaptationFirstOrderModelForm, self).__init__(are_voi_disabled)
        self.g_L = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.g_L)
        self.E_L_e = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.E_L_e)
        self.E_L_i = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.E_L_i)
        self.C_m = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.C_m)
        self.b_e = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.b_e)
        self.b_i = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.b_i)
        self.a_e = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.a_e)
        self.a_i = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.a_i)
        self.tau_w_e = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.tau_w_e)
        self.tau_w_i = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.tau_w_i)
        self.E_e = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.E_e)
        self.E_i = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.E_i)
        self.Q_e = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.Q_e)
        self.Q_i = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.Q_i)
        self.tau_e = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.tau_e)
        self.tau_i = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.tau_i)
        self.N_tot = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.N_tot)
        self.p_connect = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.p_connect)
        self.g = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.g)
        self.K_ext_e = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.K_ext_e)
        self.K_ext_i = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.K_ext_i)
        self.T = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.T)
        self.P_e = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.P_e)
        self.P_i = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.P_i)
        self.external_input_ex_ex = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.external_input_ex_ex)
        self.external_input_ex_in = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.external_input_ex_in)
        self.external_input_in_ex = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.external_input_in_ex)
        self.external_input_in_in = ArrayField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.external_input_in_in)
        self.variables_of_interest = MultiSelectField(ModelsEnum.ZERLAUT_FIRST_ORDER.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"g_L": ":math:`g_{L}`", "E_L_e": ":math:`E_{Le}`", "E_L_i": ":math:`E_{Li}`", "C_m": ":math:`C_{m}`",
                "b_e": ":math:`b_e`", "b_i": ":math:`b_i`", "a_e": ":math:`a_e`", "a_i": ":math:`a_i`",
                "tau_w_e": ":math:`tau_{we}`", "tau_w_i": ":math:`tau_{wi}`", "E_e": r":math:`E_e`",
                "E_i": ":math:`E_i`", "Q_e": r":math:`Q_e`", "Q_i": r":math:`Q_i`", "tau_e": r":math:`\tau_e`",
                "tau_i": r":math:`\tau_i`", "N_tot": ":math:`N_{tot}`", "p_connect": r":math:`\epsilon`",
                "g": ":math:`g`", "K_ext_e": ":math:`K_ext_e`", "K_ext_i": ":math:`K_ext_i`", "T": ":math:`T`",
                "external_input_ex_ex": r":math:`\nu_e^{drive}`", "external_input_ex_in": r":math:`\nu_e^{drive}`",
                "external_input_in_ex": r":math:`\nu_e^{drive}`", "external_input_in_in": r":math:`\nu_e^{drive}`"}


class ZerlautAdaptationSecondOrderModelForm(ZerlautAdaptationFirstOrderModelForm):

    def __init__(self, are_voi_disabled=False):
        super(ZerlautAdaptationSecondOrderModelForm, self).__init__(are_voi_disabled)


class MontbrioPazoRoxinModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(MontbrioPazoRoxinModelForm, self).__init__(are_voi_disabled)
        self.tau = ArrayField(ModelsEnum.MONTBRIO_PAZO_ROXIN.value.tau)
        self.I = ArrayField(ModelsEnum.MONTBRIO_PAZO_ROXIN.value.I)
        self.Delta = ArrayField(ModelsEnum.MONTBRIO_PAZO_ROXIN.value.Delta)
        self.J = ArrayField(ModelsEnum.MONTBRIO_PAZO_ROXIN.value.J)
        self.eta = ArrayField(ModelsEnum.MONTBRIO_PAZO_ROXIN.value.eta)
        self.Gamma = ArrayField(ModelsEnum.MONTBRIO_PAZO_ROXIN.value.Gamma)
        self.cr = ArrayField(ModelsEnum.MONTBRIO_PAZO_ROXIN.value.cr)
        self.cv = ArrayField(ModelsEnum.MONTBRIO_PAZO_ROXIN.value.cv)
        self.variables_of_interest = MultiSelectField(ModelsEnum.MONTBRIO_PAZO_ROXIN.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"tau": r":math:`\tau`", "I": ":math:`I_{ext}`", "Delta": r":math:`\Delta`", "J": ":math:`J`",
                "eta": r":math:`\eta`", "Gamma": r":math:`\Gamma`", "cr": ":math:`cr`", "cv": ":math:`cv`"}


class CoombesByrneModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(CoombesByrneModelForm, self).__init__(are_voi_disabled)
        self.Delta = ArrayField(ModelsEnum.COOMBES_BYRNE.value.Delta)
        self.alpha = ArrayField(ModelsEnum.COOMBES_BYRNE.value.alpha)
        self.v_syn = ArrayField(ModelsEnum.COOMBES_BYRNE.value.v_syn)
        self.k = ArrayField(ModelsEnum.COOMBES_BYRNE.value.k)
        self.eta = ArrayField(ModelsEnum.COOMBES_BYRNE.value.eta)
        self.variables_of_interest = MultiSelectField(ModelsEnum.COOMBES_BYRNE.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"Delta": r":math:`\Delta`", "alpha": r":math:`\alpha`", "v_syn": ":math:`v_{syn}`", "k": ":math:`k`",
                "eta": r":math:`\eta`"}


class CoombesByrne2DModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(CoombesByrne2DModelForm, self).__init__(are_voi_disabled)
        self.Delta = ArrayField(ModelsEnum.COOMBES_BYRNE_2D.value.Delta)
        self.v_syn = ArrayField(ModelsEnum.COOMBES_BYRNE_2D.value.v_syn)
        self.k = ArrayField(ModelsEnum.COOMBES_BYRNE_2D.value.k)
        self.eta = ArrayField(ModelsEnum.COOMBES_BYRNE_2D.value.eta)
        self.variables_of_interest = MultiSelectField(ModelsEnum.COOMBES_BYRNE_2D.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"Delta": r":math:`\Delta`", "v_syn": ":math:`v_syn`", "k": ":math:`k`", "eta": r":math:`\eta`"}


class GastSchmidtKnoscheSDModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(GastSchmidtKnoscheSDModelForm, self).__init__(are_voi_disabled)
        self.tau = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.tau)
        self.tau_A = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.tau_A)
        self.alpha = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.alpha)
        self.I = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.I)
        self.Delta = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.Delta)
        self.J = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.J)
        self.eta = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.eta)
        self.cr = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.cr)
        self.cv = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.cv)
        self.variables_of_interest = MultiSelectField(
            ModelsEnum.GAST_SCHMIDT_KNOSCHE_SD.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"tau": r":math:`\tau`", "tau_A": r":math:`\tau_A`", "alpha":  r":math:`\alpha`", "I": ":math:`I_{ext}`",
                "Delta": r":math:`\Delta`", "J": ":math:`J`", "eta": r":math:`\eta`", "cr": ":math:`cr`",
                "cv": ":math:`cv`"}


class GastSchmidtKnoscheSFModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(GastSchmidtKnoscheSFModelForm, self).__init__(are_voi_disabled)
        self.tau = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.tau)
        self.tau_A = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.tau_A)
        self.alpha = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.alpha)
        self.I = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.I)
        self.Delta = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.Delta)
        self.J = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.J)
        self.eta = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.eta)
        self.cr = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.cr)
        self.cv = ArrayField(ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.cv)
        self.variables_of_interest = MultiSelectField(
            ModelsEnum.GAST_SCHMIDT_KNOSCHE_SF.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"tau": r":math:`\tau`", "tau_A": r":math:`\tau_A`", "alpha": r":math:`\alpha`", "I": ":math:`I_{ext}`",
                "Delta": r":math:`\Delta`", "J": ":math:`J`", "eta": r":math:`\eta`", "cr": ":math:`cr`",
                "cv": ":math:`cv`"}


class DumontGutkinModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(DumontGutkinModelForm, self).__init__(are_voi_disabled)
        self.I_e = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.I_e)
        self.Delta_e = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.Delta_e)
        self.eta_e = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.eta_e)
        self.tau_e = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.tau_e)
        self.I_i = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.I_i)
        self.Delta_i = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.Delta_i)
        self.eta_i = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.eta_i)
        self.tau_i = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.tau_i)
        self.tau_s = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.tau_s)
        self.J_ee = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.J_ee)
        self.J_ei = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.J_ei)
        self.J_ie = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.J_ie)
        self.J_ii = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.J_ii)
        self.Gamma = ArrayField(ModelsEnum.DUMONT_GUTKIN.value.Gamma)
        self.variables_of_interest = MultiSelectField(ModelsEnum.DUMONT_GUTKIN.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"I_e": ":math:`I_{ext_e}`", "Delta_e": r":math:`\Delta_e`", "eta_e": r":math:`\eta_e`",
                "tau_e": r":math:`\tau_e`", "I_i": ":math:`I_{ext_i}`", "Delta_i": r":math:`\Delta_i`",
                "eta_i": r":math:`\eta_i`", "tau_i": r":math:`\tau_i`", "tau_s": r":math:`\tau_s`",
                "J_ee": ":math:`J_{ee}`", "J_ei": ":math:`J_{ei}`", "J_ie": ":math:`J_{ie}`", "J_ii": ":math:`J_{ii}`",
                "Gamma": r":math:`\Gamma`"}


class LinearModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(LinearModelForm, self).__init__(are_voi_disabled)
        self.gamma = ArrayField(ModelsEnum.LINEAR.value.gamma)
        self.variables_of_interest = MultiSelectField(ModelsEnum.LINEAR.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"gamma": r":math:`\gamma`"}


class WilsonCowanModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(WilsonCowanModelForm, self).__init__(are_voi_disabled)
        self.c_ee = ArrayField(ModelsEnum.WILSON_COWAN.value.c_ee)
        self.c_ie = ArrayField(ModelsEnum.WILSON_COWAN.value.c_ie)
        self.c_ei = ArrayField(ModelsEnum.WILSON_COWAN.value.c_ei)
        self.c_ii = ArrayField(ModelsEnum.WILSON_COWAN.value.c_ii)
        self.tau_e = ArrayField(ModelsEnum.WILSON_COWAN.value.tau_e)
        self.tau_i = ArrayField(ModelsEnum.WILSON_COWAN.value.tau_i)
        self.a_e = ArrayField(ModelsEnum.WILSON_COWAN.value.a_e)
        self.b_e = ArrayField(ModelsEnum.WILSON_COWAN.value.b_e)
        self.c_e = ArrayField(ModelsEnum.WILSON_COWAN.value.c_e)
        self.theta_e = ArrayField(ModelsEnum.WILSON_COWAN.value.theta_e)
        self.a_i = ArrayField(ModelsEnum.WILSON_COWAN.value.a_i)
        self.b_i = ArrayField(ModelsEnum.WILSON_COWAN.value.b_i)
        self.theta_i = ArrayField(ModelsEnum.WILSON_COWAN.value.theta_i)
        self.c_i = ArrayField(ModelsEnum.WILSON_COWAN.value.c_i)
        self.r_e = ArrayField(ModelsEnum.WILSON_COWAN.value.r_e)
        self.r_i = ArrayField(ModelsEnum.WILSON_COWAN.value.r_i)
        self.k_e = ArrayField(ModelsEnum.WILSON_COWAN.value.k_e)
        self.k_i = ArrayField(ModelsEnum.WILSON_COWAN.value.k_i)
        self.P = ArrayField(ModelsEnum.WILSON_COWAN.value.P)
        self.Q = ArrayField(ModelsEnum.WILSON_COWAN.value.Q)
        self.alpha_e = ArrayField(ModelsEnum.WILSON_COWAN.value.alpha_e)
        self.alpha_i = ArrayField(ModelsEnum.WILSON_COWAN.value.alpha_i)
        self.variables_of_interest = MultiSelectField(ModelsEnum.WILSON_COWAN.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"c_ee": "math:`c_{ee}`", 'c_ei': ":math:`c_{ei}`", "c_ii": ":math:`c_{ii}`",
                "tau_e": r":math:`\tau_e`", "tau_i": r":math:`\tau_i`", "a_e": ":math:`a_e`", "b_e": ":math:`b_e`",
                "c_e": ":math:`c_{ei}`", "a_i": ":math:`a_i`", "b_i": ":math:`b_i`", "c_i": ":math:`c_i`",
                "r_e": ":math:`r_e`", "r_i": ":math:`r_i`", "k_e": ":math:`k_e`", "k_i": ":math:`k_i`",
                "P": ":math:`P`", "Q": ":math:`Q`", "theta_e": r":math:`\theta_e`", "theta_i": r":math:`\theta_i",
                "alpha_e": r":math:`\alpha_e`", "alpha_i": r":math:`\alpha_i`"}


class LarterBreakspearModelForm(ModelForm):

    def __init__(self, are_voi_disabled=False):
        super(LarterBreakspearModelForm, self).__init__(are_voi_disabled)
        self.gCa = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.gCa)
        self.gK = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.gK)
        self.gL = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.gL)
        self.phi = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.phi)
        self.gNa = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.gNa)
        self.TK = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.TK)
        self.TCa = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.TCa)
        self.TNa = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.TNa)
        self.VCa = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.VCa)
        self.VK = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.VK)
        self.VL = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.VL)
        self.VNa = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.VNa)
        self.d_K = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.d_K)
        self.tau_K = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.tau_K)
        self.d_Na = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.d_Na)
        self.d_Ca = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.d_Ca)
        self.aei = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.aei)
        self.aie = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.aie)
        self.b = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.b)
        self.C = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.C)
        self.ane = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.ane)
        self.ani = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.ani)
        self.aee = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.aee)
        self.Iext = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.Iext)
        self.rNMDA = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.rNMDA)
        self.VT = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.VT)
        self.d_V = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.d_V)
        self.ZT = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.ZT)
        self.d_Z = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.d_Z)
        self.QV_max = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.QV_max)
        self.QZ_max = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.QZ_max)
        self.t_scale = ArrayField(ModelsEnum.LARTER_BREAKSPEAR.value.t_scale)
        self.variables_of_interest = MultiSelectField(ModelsEnum.LARTER_BREAKSPEAR.value.variables_of_interest)

    @staticmethod
    def get_params_configurable_in_phase_plane():
        return {"gCa": ":math:`g_{Ca}`", "gK": ":math:`g_{K}`", "gL": ":math:`g_{L}`", "phi": r":math:`\phi`",
                "gNa": ":math:`g_{Na}`", "TK": ":math:`T_{K}`", "TCa": ":math:`T_{Ca}`", "TNa": ":math:`T_{Na}`",
                "VCa": ":math:`V_{Ca}`", "VK": ":math:`V_{K}`", "VL": ":math:`V_{L}`", "VNa": ":math:`V_{Na}`",
                "d_K": r":math:`\delta_{K}`", "tau_K": r":math:`\tau_{K}`", "d_Na": r":math:`\delta_{Na}`",
                "d_Ca": r":math:`\delta_{Ca}`", "aei": ":math:`a_{ei}`", "aie": ":math:`a_{ie}`", "b": ":math:`b`",
                "C": ":math:`C`", "ane": ":math:`a_{ne}`", "ani": ":math:`a_{ni}`", "aee": ":math:`a_{ee}`",
                "Iext": ":math:`I_{ext}`", "rNMDA": ":math:`r_{NMDA}`", "VT": ":math:`V_{T}`",
                "d_V": r":math:`\delta_{V}`", "ZT": ":math:`Z_{T}`", "d_Z": r":math:`\delta_{Z}`",
                "QV_max": ":math:`QV_{max}`", "QZ_max": ":math:`QZ_{max}`", "t_scale": ":math:`t_{scale}`"}
