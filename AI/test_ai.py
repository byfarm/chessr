import pytest
import ai
import rules_and_func.game
import numpy as np
from ai_train import train_ai, assign_winner



def test_bits():
	game = rules_and_func.game.MachineBoard()
	bitboard = ai.to_bits(game)
	assert bitboard.shape == (232, 8, 8)


def test_train_ai():
 value_net = ai.value_NN()
 policy_net = ai.policy_NN()
 examples = [[np.array([[[[1, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 1, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 1, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 1]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 1, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 1, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]]]), [0.004467456, 0.0046322905, 0.0045985053, 0.0044603846, 0.0045860154, 0.004604389, 0.0046132053, 0.004621476, 0.004629223, 0.0045953784, 0.004713807, 0.0045048934, 0.004704637, 0.0045451345, 0.004612715, 0.004601663, 0.004700882, 0.0045984974, 0.004653204, 0.004459509, 0.0046228683, 0.0045457603, 0.004610421, 0.004675009, 0.004692488, 0.0045445994, 0.004490784, 0.004590709, 0.004759107, 0.004810155, 0.004518277, 0.004514485, 0.004585199, 0.0046729133, 0.0045007216, 0.0045269593, 0.004638809, 0.004568869, 0.004354163, 0.004571209, 0.004727874, 0.0047472436, 0.0046836245, 0.004750573, 0.004512688, 0.0045645107, 0.004438312, 0.004495109, 0.0046808803, 0.0045418036, 0.0047111036, 0.004586046, 0.004519221, 0.0045908336, 0.0046498207, 0.0046698996, 0.0045865607, 0.0047748005, 0.0045950706, 0.004585303, 0.0045284703, 0.00459926, 0.004476528, 0.004528521, 0.0044417097, 0.0047139637, 0.0045739277, 0.004582069, 0.004559322, 0.004564802, 0.004643842, 0.004679964, 0.004453769, 0.004561807, 0.004627966, 0.0045427787, 0.0045025046, 0.0044282908, 0.0045572375, 0.0046125534, 0.004565635, 0.0045867832, 0.0046304734, 0.0046884385, 0.0045243297, 0.004404496, 0.004713638, 0.004731328, 0.004453826, 0.004468583, 0.004574209, 0.004770255, 0.004511145, 0.0046230936, 0.0046540177, 0.0045866105, 0.0044460013, 0.00469583, 0.004628583, 0.004518617, 0.0046001105, 0.004767351, 0.004586707, 0.004528899, 0.004466183, 0.004687592, 0.004560172, 0.0045860093, 0.0045119803, 0.004544025, 0.004549258, 0.004624645, 0.0045448067, 0.0047308477, 0.004489022, 0.0044941204, 0.004691121, 0.0045600217, 0.004590864, 0.0045499834, 0.0045064003, 0.004589653, 0.0045606797, 0.004485953, 0.0046112337, 0.0045727612, 0.0045674886, 0.00469315, 0.004452843, 0.004570048, 0.0044883895, 0.0047021606, 0.0047000507, 0.0045880266, 0.0045730392, 0.004726548, 0.004631708, 0.004479201, 0.0046289684, 0.004669871, 0.004551474, 0.004428168, 0.004543109, 0.004566397, 0.004490214, 0.004679385, 0.0046512843, 0.0045915577, 0.0044406187, 0.004530231, 0.0046484144, 0.004694524, 0.004570781, 0.0046578837, 0.0046304986, 0.0045515294, 0.004499827, 0.0045335866, 0.0046135425, 0.0045833252, 0.0045772367, 0.0045819413, 0.00467576, 0.0046043526, 0.004444525, 0.0046509146, 0.0046003275, 0.0046737306, 0.00450795, 0.0044920132, 0.004601513, 0.0046157525, 0.0046511595, 0.0045724353, 0.0046437085, 0.0047099986, 0.004602219, 0.0044524483, 0.0045561437, 0.0045216903, 0.0046705706, 0.0045571723, 0.004706112, 0.004607967, 0.0046802294, 0.0045640934, 0.004586993, 0.004625143, 0.004693238, 0.004572228, 0.0046269973, 0.004494741, 0.0047019795, 0.0046370183, 0.0046687657, 0.0045579267, 0.0045233606, 0.0045951414, 0.0046214904, 0.004506373, 0.0045356695, 0.0046936334, 0.0045257816, 0.0044541853, 0.004447666, 0.0045674946, 0.004708132, 0.004577321, 0.0045462516, 0.0045173895, 0.0046384046, 0.0045868238, 0.0044957707, 0.0044954866, 0.00472209, 0.004504953, 0.0044528656, 0.004615219], 0.26386106, None],
[np.array([[[[1, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 1, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 1, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 1]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 1, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 1, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0],
                  [1, 1, 1, 1, 1, 0, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]],

              [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0],
                  [1, 1, 1, 1, 1, 0, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]]]),
  [0.0045232857, 0.004601263, 0.0045428434, 0.0045271395, 0.0045686876, 0.00457829, 0.0045517315, 0.0045624794, 0.004553321, 0.0046038753, 0.0046810787, 0.0045485557, 0.0046403753, 0.0045974706, 0.004557504, 0.004604877, 0.0046296013, 0.0046011615, 0.004659297, 0.0045644804, 0.00461901, 0.004585772, 0.0045856372, 0.004640827, 0.0046332283, 0.00457758, 0.0045507415, 0.0046191853, 0.00468939, 0.004706576, 0.0045269667, 0.00455073, 0.0045763864, 0.004636602, 0.004531499, 0.004519057, 0.0046045464, 0.0045557925, 0.00447957, 0.0045753135, 0.0046819765, 0.004695751, 0.00462194, 0.004676351, 0.0045799394, 0.004531659, 0.004547351, 0.004527744, 0.0046434295, 0.0045766663, 0.0046663797, 0.004616698, 0.0045527774, 0.004566474, 0.0046392004, 0.0046207667, 0.004573576, 0.004692687, 0.004603037, 0.004570655, 0.0045671538, 0.004572193, 0.0045314063, 0.004531648, 0.004509484, 0.004633686, 0.004563874, 0.0046356763, 0.0045368765, 0.0045630937, 0.0046362006, 0.0046352185, 0.004539876, 0.004563163, 0.004631676, 0.0046090093, 0.004579321, 0.004489439, 0.004556183, 0.0045596007, 0.004577934, 0.0046257223, 0.00463661, 0.0046774214, 0.0045844833, 0.00446812, 0.004643353, 0.004659737, 0.0045261816, 0.0045495043, 0.0045729266, 0.0046276054, 0.0045516747, 0.0045922976, 0.0046507977, 0.0045925537, 0.0045768763, 0.004628183, 0.0046227747, 0.004551987, 0.004650809, 0.004685033, 0.0046043983, 0.004527587, 0.0045507783, 0.0046462244, 0.0045381114, 0.0045977496, 0.0045899623, 0.0045745648, 0.0045019817, 0.0045916927, 0.0045338017, 0.0047058756, 0.0045257914, 0.004548324, 0.0046347072, 0.004619036, 0.0046077226, 0.0045172726, 0.004502174, 0.004572821, 0.0045745894, 0.004515599, 0.004609069, 0.004533875, 0.004595998, 0.004676809, 0.0045234542, 0.004541276, 0.0045244107, 0.0045955274, 0.0046430705, 0.0046000243, 0.0045909323, 0.004621687, 0.00460453, 0.004528929, 0.0046191253, 0.0046281987, 0.0045500468, 0.0044986266, 0.004545131, 0.0045661847, 0.004533547, 0.0046169236, 0.0046380134, 0.004604402, 0.004531657, 0.0045937006, 0.004568132, 0.0046571516, 0.0045984793, 0.0046078223, 0.0046255663, 0.0045561404, 0.0045403764, 0.0045794756, 0.0045965724, 0.0046247486, 0.0046241363, 0.0045520687, 0.0046391585, 0.004596677, 0.0045075524, 0.004615777, 0.0046265367, 0.0046349717, 0.004587089, 0.0045418544, 0.0045696055, 0.0045867017, 0.004674704, 0.0045735226, 0.0045908107, 0.004640911, 0.0046021556, 0.00450522, 0.004595657, 0.0045334753, 0.00458891, 0.004556027, 0.0046462636, 0.0045777457, 0.0046576783, 0.0045527476, 0.004581941, 0.004585091, 0.004612358, 0.0045370813, 0.004629276, 0.0045586894, 0.004647757, 0.0045955316, 0.004653018, 0.0046116807, 0.0045153624, 0.0046039238, 0.004645606, 0.004574522, 0.0045620655, 0.004658932, 0.004528082, 0.0045463084, 0.0045099184, 0.004560604, 0.0046599195, 0.0045833695, 0.004606933, 0.0045293747, 0.0045808395, 0.004563982, 0.004534368, 0.004569753, 0.0046247817, 0.0045519606, 0.0045342366, 0.0045702974], 0.0856665, None]]
 examples = assign_winner(examples, True)
 train_ai(examples, value_net, policy_net=policy_net)
