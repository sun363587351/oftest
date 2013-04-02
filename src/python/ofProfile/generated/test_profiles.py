# ./test_profiles.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2013-04-01 02:06:24.607389 by PyXB version 1.2.1
# Namespace AbsentNamespace0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:48728216-9a92-11e2-9fbd-4ceb4290010f')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 4, 2)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element test_profile uses Python identifier test_profile
    __test_profile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'test_profile'), 'test_profile', '__AbsentNamespace0_CTD_ANON_test_profile', True, pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 6, 4), )

    
    test_profile = property(__test_profile.value, __test_profile.set, None, None)


    _ElementMap = {
        __test_profile.name() : __test_profile
    }
    _AttributeMap = {
        
    }



# Complex type test_profile_type with content type ELEMENT_ONLY
class test_profile_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type test_profile_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'test_profile_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 10, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element test uses Python identifier test
    __test = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'test'), 'test', '__AbsentNamespace0_test_profile_type_test', True, pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 12, 3), )

    
    test = property(__test.value, __test.set, None, None)


    _ElementMap = {
        __test.name() : __test
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'test_profile_type', test_profile_type)


# Complex type test_type with content type ELEMENT_ONLY
class test_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type test_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'test_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 15, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element match_fields uses Python identifier match_fields
    __match_fields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'match_fields'), 'match_fields', '__AbsentNamespace0_test_type_match_fields', True, pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 17, 4), )

    
    match_fields = property(__match_fields.value, __match_fields.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_test_type_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 19, 24)
    __name._UseLocation = pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 19, 24)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __match_fields.name() : __match_fields
    }
    _AttributeMap = {
        __name.name() : __name
    }
Namespace.addCategoryObject('typeBinding', u'test_type', test_type)


# Complex type match_fields_type with content type ELEMENT_ONLY
class match_fields_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type match_fields_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'match_fields_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 21, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element match_field uses Python identifier match_field
    __match_field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'match_field'), 'match_field', '__AbsentNamespace0_match_fields_type_match_field', True, pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 23, 3), )

    
    match_field = property(__match_field.value, __match_field.set, None, None)


    _ElementMap = {
        __match_field.name() : __match_field
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'match_fields_type', match_fields_type)


# Complex type match_field_type with content type ELEMENT_ONLY
class match_field_type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type match_field_type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'match_field_type')
    _XSDLocation = pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 27, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element property_name uses Python identifier property_name
    __property_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'property_name'), 'property_name', '__AbsentNamespace0_match_field_type_property_name', False, pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 29, 4), )

    
    property_name = property(__property_name.value, __property_name.set, None, None)

    
    # Element property_value uses Python identifier property_value
    __property_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'property_value'), 'property_value', '__AbsentNamespace0_match_field_type_property_value', False, pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 30, 4), )

    
    property_value = property(__property_value.value, __property_value.set, None, None)


    _ElementMap = {
        __property_name.name() : __property_name,
        __property_value.name() : __property_value
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'match_field_type', match_field_type)


test_profiles = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'test_profiles'), CTD_ANON, location=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 3, 1))
Namespace.addCategoryObject('elementBinding', test_profiles.name().localName(), test_profiles)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'test_profile'), test_profile_type, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 6, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 6, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'test_profile')), pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 6, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




test_profile_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'test'), test_type, scope=test_profile_type, location=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 12, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 12, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(test_profile_type._UseForTag(pyxb.namespace.ExpandedName(None, u'test')), pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 12, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
test_profile_type._Automaton = _BuildAutomaton_()




test_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'match_fields'), match_fields_type, scope=test_type, location=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 17, 4)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 17, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(test_type._UseForTag(pyxb.namespace.ExpandedName(None, u'match_fields')), pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
test_type._Automaton = _BuildAutomaton_2()




match_fields_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'match_field'), match_field_type, scope=match_fields_type, location=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 23, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 23, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(match_fields_type._UseForTag(pyxb.namespace.ExpandedName(None, u'match_field')), pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 23, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
match_fields_type._Automaton = _BuildAutomaton_3()




match_field_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'property_name'), pyxb.binding.datatypes.string, scope=match_field_type, location=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 29, 4)))

match_field_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'property_value'), pyxb.binding.datatypes.string, scope=match_field_type, location=pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 30, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(match_field_type._UseForTag(pyxb.namespace.ExpandedName(None, u'property_name')), pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 29, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(match_field_type._UseForTag(pyxb.namespace.ExpandedName(None, u'property_value')), pyxb.utils.utility.Location('/home/abhy/oftest_new/oftest/src/python/ofProfile/src/python/profile/test_profiles.xsd', 30, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
match_field_type._Automaton = _BuildAutomaton_4()
