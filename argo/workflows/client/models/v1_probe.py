# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: master
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Probe(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'failure_threshold': 'int',
        'handler': 'V1Handler',
        'initial_delay_seconds': 'int',
        'period_seconds': 'int',
        'success_threshold': 'int',
        'timeout_seconds': 'int'
    }

    attribute_map = {
        'failure_threshold': 'failureThreshold',
        'handler': 'handler',
        'initial_delay_seconds': 'initialDelaySeconds',
        'period_seconds': 'periodSeconds',
        'success_threshold': 'successThreshold',
        'timeout_seconds': 'timeoutSeconds'
    }

    def __init__(self, failure_threshold=None, handler=None, initial_delay_seconds=None, period_seconds=None, success_threshold=None, timeout_seconds=None):  # noqa: E501
        """V1Probe - a model defined in Swagger"""  # noqa: E501

        self._failure_threshold = None
        self._handler = None
        self._initial_delay_seconds = None
        self._period_seconds = None
        self._success_threshold = None
        self._timeout_seconds = None
        self.discriminator = None

        if failure_threshold is not None:
            self.failure_threshold = failure_threshold
        if handler is not None:
            self.handler = handler
        if initial_delay_seconds is not None:
            self.initial_delay_seconds = initial_delay_seconds
        if period_seconds is not None:
            self.period_seconds = period_seconds
        if success_threshold is not None:
            self.success_threshold = success_threshold
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds

    @property
    def failure_threshold(self):
        """Gets the failure_threshold of this V1Probe.  # noqa: E501


        :return: The failure_threshold of this V1Probe.  # noqa: E501
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """Sets the failure_threshold of this V1Probe.


        :param failure_threshold: The failure_threshold of this V1Probe.  # noqa: E501
        :type: int
        """

        self._failure_threshold = failure_threshold

    @property
    def handler(self):
        """Gets the handler of this V1Probe.  # noqa: E501


        :return: The handler of this V1Probe.  # noqa: E501
        :rtype: V1Handler
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this V1Probe.


        :param handler: The handler of this V1Probe.  # noqa: E501
        :type: V1Handler
        """

        self._handler = handler

    @property
    def initial_delay_seconds(self):
        """Gets the initial_delay_seconds of this V1Probe.  # noqa: E501


        :return: The initial_delay_seconds of this V1Probe.  # noqa: E501
        :rtype: int
        """
        return self._initial_delay_seconds

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, initial_delay_seconds):
        """Sets the initial_delay_seconds of this V1Probe.


        :param initial_delay_seconds: The initial_delay_seconds of this V1Probe.  # noqa: E501
        :type: int
        """

        self._initial_delay_seconds = initial_delay_seconds

    @property
    def period_seconds(self):
        """Gets the period_seconds of this V1Probe.  # noqa: E501


        :return: The period_seconds of this V1Probe.  # noqa: E501
        :rtype: int
        """
        return self._period_seconds

    @period_seconds.setter
    def period_seconds(self, period_seconds):
        """Sets the period_seconds of this V1Probe.


        :param period_seconds: The period_seconds of this V1Probe.  # noqa: E501
        :type: int
        """

        self._period_seconds = period_seconds

    @property
    def success_threshold(self):
        """Gets the success_threshold of this V1Probe.  # noqa: E501


        :return: The success_threshold of this V1Probe.  # noqa: E501
        :rtype: int
        """
        return self._success_threshold

    @success_threshold.setter
    def success_threshold(self, success_threshold):
        """Sets the success_threshold of this V1Probe.


        :param success_threshold: The success_threshold of this V1Probe.  # noqa: E501
        :type: int
        """

        self._success_threshold = success_threshold

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this V1Probe.  # noqa: E501


        :return: The timeout_seconds of this V1Probe.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this V1Probe.


        :param timeout_seconds: The timeout_seconds of this V1Probe.  # noqa: E501
        :type: int
        """

        self._timeout_seconds = timeout_seconds

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1Probe, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1Probe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
