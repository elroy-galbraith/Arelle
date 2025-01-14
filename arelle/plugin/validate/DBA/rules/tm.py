"""
See COPYRIGHT.md for copyright information.
"""
from __future__ import annotations

import datetime
import decimal
import itertools
from collections.abc import Iterable
from typing import Any, cast

from arelle.typing import TypeGetText
from arelle.ValidateXbrl import ValidateXbrl
from arelle.utils.PluginHooks import ValidationHook
from arelle.utils.validate.Decorator import validation
from arelle.utils.validate.Validation import Validation
from arelle.XmlValidateConst import VALID
from . import errorOnDateFactComparison, errorOnRequiredFact, getFactsWithDimension, getFactsGroupedByContextId, errorOnRequiredPositiveFact
from ..PluginValidationDataExtension import PluginValidationDataExtension
from ..ValidationPluginExtension import DANISH_CURRENCY_ID, ROUNDING_MARGIN, PERSONNEL_EXPENSE_THRESHOLD

_: TypeGetText


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm13(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM13: gsd:IdentificationNumberCvrOfReportingEntity must only be tagged once if tagged
    """
    modelXbrl = val.modelXbrl
    facts = modelXbrl.factsByQname.get(pluginData.identificationNumberCvrOfReportingEntityQn)
    if facts is not None and len(facts) > 1:
        yield Validation.error(
            'DBA.TM13',
            _('IdentificationNumberCvrOfReportingEntity must only be tagged once. {} facts were found.').format(len(facts)),
            modelObject=facts
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm16(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM16: gsd:InformationOnTypeOfSubmittedReport must only be tagged once if tagged
    """
    modelXbrl = val.modelXbrl
    facts = modelXbrl.factsByQname.get(pluginData.informationOnTypeOfSubmittedReportQn)
    if facts is not None and len(facts) > 1:
        yield Validation.error(
            'DBA.TM16',
            _('InformationOnTypeOfSubmittedReport must only be tagged once. {} facts were found.').format(len(facts)),
            modelObject=facts
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm18(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM18: ReportingPeriodStartDate with either no dimensionality or with the default dimension of
    TypeOfReportingPeriodDimension:AllReportingPeriodsMember must only be tagged once.
    """
    modelXbrl = val.modelXbrl
    valid_facts = []
    start_date_facts = modelXbrl.factsByQname.get(pluginData.reportingPeriodStartDateQn)
    if start_date_facts is not None:
        for fact in start_date_facts:
            if not fact.context.scenDimValues:
                valid_facts.append(fact)
        if len(valid_facts) > 1:
            yield Validation.error(
                'DBA.TM18',
                _('ReportingPeriodStartDate with either no dimensionality or with the default dimension of '
                  'TypeOfReportingPeriodDimension:AllReportingPeriodsMember must only be tagged once. {} facts '
                  'were found.').format(len(valid_facts)),
                modelObject=valid_facts
            )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm20(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM20: ReportingPeriodEndDate with either no dimensionality or with the default dimension of
    TypeOfReportingPeriodDimension:AllReportingPeriodsMember must only be tagged once.
    """
    modelXbrl = val.modelXbrl
    valid_facts = []
    end_date_facts = modelXbrl.factsByQname.get(pluginData.reportingPeriodEndDateQn)
    if end_date_facts is not None:
        for fact in end_date_facts:
            if not fact.context.scenDimValues:
                valid_facts.append(fact)
        if len(valid_facts) > 1:
            yield Validation.error(
                'DBA.TM20',
                _('ReportingPeriodEndDate with either no dimensionality or with the default dimension of '
                  'TypeOfReportingPeriodDimension:AllReportingPeriodsMember must only be tagged once. {} facts '
                  'were found.').format(len(valid_facts)),
                modelObject=valid_facts
            )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm22(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM22: gsd:NameOfReportingEntity must only be tagged once if tagged
    """
    modelXbrl = val.modelXbrl
    facts = modelXbrl.factsByQname.get(pluginData.nameOfReportingEntityQn)
    if facts is not None and len(facts) > 1:
        yield Validation.error(
            'DBA.TM22',
            _('NameOfReportingEntity must only be tagged once. {} facts were found.').format(len(facts)),
            modelObject=facts
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm24(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM24: gsd:NameOfSubmittingEnterprise must only be tagged once if tagged
    """
    modelXbrl = val.modelXbrl
    facts = modelXbrl.factsByQname.get(pluginData.nameOfSubmittingEnterpriseQn)
    if facts is not None and len(facts) > 1:
        yield Validation.error(
            'DBA.TM24',
            _('NameOfSubmittingEnterprise must only be tagged once. {} facts were found.').format(len(facts)),
            modelObject=facts
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm26(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM26: gsd:AddressOfSubmittingEnterpriseStreetAndNumber must only be tagged once if tagged
    """
    modelXbrl = val.modelXbrl
    facts = modelXbrl.factsByQname.get(pluginData.addressOfSubmittingEnterpriseStreetAndNumberQn)
    if facts is not None and len(facts) > 1:
        yield Validation.error(
            'DBA.TM26',
            _('AddressOfSubmittingEnterpriseStreetAndNumber must only be tagged once. {} facts were found.').format(len(facts)),
            modelObject=facts
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm28(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM28: gsd:AddressOfSubmittingEnterprisePostcodeAndTown must only be tagged once if tagged
    """
    modelXbrl = val.modelXbrl
    facts = modelXbrl.factsByQname.get(pluginData.addressOfSubmittingEnterprisePostcodeAndTownQn)
    if facts is not None and len(facts) > 1:
        yield Validation.error(
            'DBA.TM28',
            _('AddressOfSubmittingEnterprisePostcodeAndTown must only be tagged once. {} facts were found.').format(len(facts)),
            modelObject=facts
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm29(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM29: Either gsd:DateOfGeneralMeeting or gsd:DateOfApprovalOfReport must be specified
    """
    modelXbrl = val.modelXbrl
    meeting_facts = modelXbrl.factsByQname.get(pluginData.dateOfGeneralMeetingQn)
    approval_facts = modelXbrl.factsByQname.get(pluginData.dateOfApprovalOfReportQn)
    if meeting_facts is None and approval_facts is None:
        yield Validation.error(
            'DBA.TM29',
            _('Either DateOfGeneralMeeting or DateOfApprovalOfReport must be tagged in the document.')
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm30(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM30: gsd:DateOfGeneralMeeting must only be tagged once if tagged
    """
    modelXbrl = val.modelXbrl
    facts = modelXbrl.factsByQname.get(pluginData.dateOfGeneralMeetingQn)
    if facts is not None and len(facts) > 1:
        yield Validation.error(
            'DBA.TM30',
            _('DateOfGeneralMeeting must only be tagged once. {} facts were found.').format(len(facts)),
            modelObject=facts
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm31(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM31: gsd:DateOfApprovalOfReport must only be tagged once if tagged
    """
    modelXbrl = val.modelXbrl
    facts = modelXbrl.factsByQname.get(pluginData.dateOfApprovalOfReportQn)
    if facts is not None and len(facts) > 1:
        yield Validation.error(
            'DBA.TM31',
            _('DateOfApprovalOfReport must only be tagged once. {} facts were found.').format(len(facts)),
            modelObject=facts
        )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm32(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM33: ReportingPeriodStartDate with the dimension of
    TypeOfReportingPeriodDimension:RegisteredReportingPeriodDeviatingFromReportedReportingPeriodDueArbitraryDatesMember
    must only be tagged once.
    """
    modelXbrl = val.modelXbrl
    valid_facts = []
    start_date_facts = modelXbrl.factsByQname.get(pluginData.reportingPeriodStartDateQn)
    if start_date_facts is not None:
        for fact in start_date_facts:
            member = fact.context.qnameDims.get(pluginData.typeOfReportingPeriodDimensionQn)
            if member is not None and member.memberQname == pluginData.registeredReportingPeriodDeviatingFromReportedReportingPeriodDueArbitraryDatesMemberQn:
                valid_facts.append(fact)
        if len(valid_facts) > 1:
            yield Validation.error(
                'DBA.TM32',
                _('ReportingPeriodStartDate with the dimension of TypeOfReportingPeriodDimension:RegisteredReportingPeriodDeviatingFromReportedReportingPeriodDueArbitraryDatesMember '
                  'must only be tagged once. {} facts were found.').format(len(valid_facts)),
                modelObject=valid_facts
            )


@validation(
    hook=ValidationHook.XBRL_FINALLY,
)
def rule_tm33(
        pluginData: PluginValidationDataExtension,
        val: ValidateXbrl,
        *args: Any,
        **kwargs: Any,
) -> Iterable[Validation]:
    """
    DBA.TM33: ReportingPeriodEndDate with the dimension of
    TypeOfReportingPeriodDimension:RegisteredReportingPeriodDeviatingFromReportedReportingPeriodDueArbitraryDatesMember
    must only be tagged once.
    """
    modelXbrl = val.modelXbrl
    valid_facts = []
    end_date_facts = modelXbrl.factsByQname.get(pluginData.reportingPeriodEndDateQn)
    if end_date_facts is not None:
        for fact in end_date_facts:
            member = fact.context.qnameDims.get(pluginData.typeOfReportingPeriodDimensionQn)
            if member is not None and member.memberQname == pluginData.registeredReportingPeriodDeviatingFromReportedReportingPeriodDueArbitraryDatesMemberQn:
                valid_facts.append(fact)
        if len(valid_facts) > 1:
            yield Validation.error(
                'DBA.TM33',
                _('ReportingPeriodEndDate with the dimension of TypeOfReportingPeriodDimension:RegisteredReportingPeriodDeviatingFromReportedReportingPeriodDueArbitraryDatesMember '
                  'must only be tagged once. {} facts were found.').format(len(valid_facts)),
                modelObject=valid_facts
            )
