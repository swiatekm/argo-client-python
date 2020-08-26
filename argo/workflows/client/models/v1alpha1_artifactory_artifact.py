# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.10.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration

from kubernetes.client.models import V1SecretKeySelector


class V1alpha1ArtifactoryArtifact(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'password_secret': 'V1SecretKeySelector',
        'url': 'str',
        'username_secret': 'V1SecretKeySelector'
    }

    attribute_map = {
        'password_secret': 'passwordSecret',
        'url': 'url',
        'username_secret': 'usernameSecret'
    }

    def __init__(self, password_secret=None, url=None, username_secret=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ArtifactoryArtifact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._password_secret = None
        self._url = None
        self._username_secret = None
        self.discriminator = None

        if password_secret is not None:
            self.password_secret = password_secret
        self.url = url
        if username_secret is not None:
            self.username_secret = username_secret

    @property
    def password_secret(self):
        """Gets the password_secret of this V1alpha1ArtifactoryArtifact.  # noqa: E501


        :return: The password_secret of this V1alpha1ArtifactoryArtifact.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._password_secret

    @password_secret.setter
    def password_secret(self, password_secret):
        """Sets the password_secret of this V1alpha1ArtifactoryArtifact.


        :param password_secret: The password_secret of this V1alpha1ArtifactoryArtifact.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._password_secret = password_secret

    @property
    def url(self):
        """Gets the url of this V1alpha1ArtifactoryArtifact.  # noqa: E501

        URL of the artifact  # noqa: E501

        :return: The url of this V1alpha1ArtifactoryArtifact.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1alpha1ArtifactoryArtifact.

        URL of the artifact  # noqa: E501

        :param url: The url of this V1alpha1ArtifactoryArtifact.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def username_secret(self):
        """Gets the username_secret of this V1alpha1ArtifactoryArtifact.  # noqa: E501


        :return: The username_secret of this V1alpha1ArtifactoryArtifact.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._username_secret

    @username_secret.setter
    def username_secret(self, username_secret):
        """Sets the username_secret of this V1alpha1ArtifactoryArtifact.


        :param username_secret: The username_secret of this V1alpha1ArtifactoryArtifact.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._username_secret = username_secret

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1ArtifactoryArtifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ArtifactoryArtifact):
            return True

        return self.to_dict() != other.to_dict()
