from typing import List

from eisp.param._param import _param
from eisp.utils import concretemethod, instance, logger


class data_host(_param):
  '''
  todo: docs
  '''

  @concretemethod
  def _parse(self, params: List[str]) -> None:
    '''
    todo: docs
    '''
    instance.config.set('data', 'host', params[0])
    logger().info('Set data host to %s', params[0])
