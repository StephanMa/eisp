from typing import List

from eisp.param._param import _param
from eisp.utils import concretemethod, instance, logger


class data_root(_param):
  '''
  todo: docs
  '''

  @concretemethod
  def _parse(self, params: List[str]) -> None:
    '''
    todo: docs
    '''
    instance.config.set('data', 'root', params[0])
    logger().info('Set data root to %s', params[0])
