^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package rosidl_runtime_py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.8.0 (2019-09-26)
------------------
* install resource marker file for package (`#2 <https://github.com/ros2/rosidl_runtime_py/issues/2>`_)
* Update setup.py URLs
* Add contributing and license files
* install package manifest (`ros2/rosidl_python#86 <https://github.com/ros2/rosidl_python/issues/86>`_)
* Rename TestConfig class to Config to avoid pytest warning (`ros2/rosidl_python#82 <https://github.com/ros2/rosidl_python/issues/82>`_)
* fix set_message_fields for numpy array (`ros2/rosidl_python#81 <https://github.com/ros2/rosidl_python/issues/81>`_)
* Fix type name queries for string types. (`ros2/rosidl_python#77 <https://github.com/ros2/rosidl_python/issues/77>`_)
* Require keyword arguments be passed by name (`ros2/rosidl_python#80 <https://github.com/ros2/rosidl_python/issues/80>`_)
* Add utility functions to get interface from identifier
* Make import_message_from_namespaced_type operate on NamespacedType (`ros2/rosidl_python#74 <https://github.com/ros2/rosidl_python/issues/74>`_)
* handle set_message_fields given some non-basic type (`ros2/rosidl_python#68 <https://github.com/ros2/rosidl_python/issues/68>`_)
* Add no_arr and no_str parameters (`ros2/rosidl_python#38 <https://github.com/ros2/rosidl_python/issues/38>`_)
* Contributors: Dirk Thomas, Jacob Perron, Jeremie Deray, Michel Hidalgo, Mikael Arguedas, Vinnam Kim, ivanpauno

0.7.6 (2019-05-30)
------------------
* fix logic around populating arrays (`ros2/rosidl_python#62 <https://github.com/ros2/rosidl_python/issues/62>`_)
* Fix the setting of array variables. (`ros2/rosidl_python#59 <https://github.com/ros2/rosidl_python/issues/59>`_)
* Contributors: Chris Lalancette, Dirk Thomas

0.7.5 (2019-05-29)
------------------

0.7.4 (2019-05-20)
------------------

0.7.3 (2019-05-08 17:57)
------------------------

0.7.2 (2019-05-08 16:58)
------------------------
* allow unicode chars in yaml output (`ros2/rosidl_python#50 <https://github.com/ros2/rosidl_python/issues/50>`_)
* add xmllint linter test (`ros2/rosidl_python#53 <https://github.com/ros2/rosidl_python/issues/53>`_)
* store types as tuple of abstract types (`ros2/rosidl_python#33 <https://github.com/ros2/rosidl_python/issues/33>`_)
* Update tests that were missed during switch to use new interfaces (`ros2/rosidl_python#51 <https://github.com/ros2/rosidl_python/issues/51>`_)
* [rosidl_runtime_py] Use new test interface definitions
* simplify code using updated definition API (`ros2/rosidl_python#45 <https://github.com/ros2/rosidl_python/issues/45>`_)
* Contributors: Dirk Thomas, Jacob Perron, Mikael Arguedas

0.7.1 (2019-04-14 12:48)
------------------------

0.7.0 (2019-04-14 05:05)
------------------------
* fix echo of numpy.number values (`ros2/rosidl_python#37 <https://github.com/ros2/rosidl_python/issues/37>`_)
* Refactor rosidl_runtime_py functions
* Add rosidl_runtime_py package
* Contributors: Dirk Thomas, Jacob Perron
