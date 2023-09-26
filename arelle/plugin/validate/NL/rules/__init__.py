from arelle.ModelValue import qname
from arelle.plugin.validate.NL.DisclosureSystems import DISCLOSURE_SYSTEM_NT16, DISCLOSURE_SYSTEM_NT17, DISCLOSURE_SYSTEM_NT18

NT16_ENTRYPOINT_ROOT = 'http://www.nltaxonomie.nl/nt16/kvk/20211208/entrypoints/'
NT17_ENTRYPOINT_ROOT = 'http://www.nltaxonomie.nl/nt17/kvk/20221214/entrypoints/'
NT18_ENTRYPOINT_ROOT = 'http://www.nltaxonomie.nl/nt18/kvk/20231213.b/entrypoints/'

NL_ENTRYPOINT_ROOTS = {
    DISCLOSURE_SYSTEM_NT16: NT16_ENTRYPOINT_ROOT,
    DISCLOSURE_SYSTEM_NT17: NT17_ENTRYPOINT_ROOT,
    DISCLOSURE_SYSTEM_NT18: NT18_ENTRYPOINT_ROOT,
}

NL_ENTRYPOINTS = {
    DISCLOSURE_SYSTEM_NT16: {NT16_ENTRYPOINT_ROOT + e for e in [
        'kvk-rpt-jaarverantwoording-2021-ifrs-full.xsd',
        'kvk-rpt-jaarverantwoording-2021-ifrs-geconsolideerd-nlgaap-enkelvoudig.xsd',
        'kvk-rpt-jaarverantwoording-2021-ifrs-smes.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-banken.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-beleggingsentiteiten.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-cooperaties.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-cv-vof.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-fondsenwervende-organisaties-klein.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-fondsenwervende-organisaties.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-groot-verticaal.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-groot.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-klein-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-klein-verticaal-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-klein-verticaal.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-klein.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-micro-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-micro.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-middelgroot-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-middelgroot-verticaal-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-middelgroot-verticaal.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-middelgroot.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-organisaties-zonder-winststreven-klein.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-organisaties-zonder-winststreven.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-pensioenfondsen.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-premiepensioeninstellingen.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-stichtingen.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-toegelaten-instellingen-volkshuisvesting.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-verzekeringsmaatschappijen.xsd',
        'kvk-rpt-jaarverantwoording-2021-nlgaap-zorginstellingen.xsd',
    ]},
    DISCLOSURE_SYSTEM_NT17: {NT17_ENTRYPOINT_ROOT + e for e in [
        'kvk-rpt-jaarverantwoording-2022-ifrs-full.xsd',
        'kvk-rpt-jaarverantwoording-2022-ifrs-geconsolideerd-nlgaap-enkelvoudig.xsd',
        'kvk-rpt-jaarverantwoording-2022-ifrs-smes.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-banken.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-beleggingsentiteiten.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-cooperaties.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-cv-vof.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-fondsenwervende-organisaties-klein.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-fondsenwervende-organisaties.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-groot-verticaal.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-groot.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-klein-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-klein-verticaal-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-klein-verticaal.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-klein.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-micro-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-micro.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-middelgroot-plus.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-middelgroot-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-middelgroot-verticaal-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-middelgroot-verticaal.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-middelgroot.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-organisaties-zonder-winststreven-klein.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-organisaties-zonder-winststreven.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-pensioenfondsen.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-premiepensioeninstellingen.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-stichtingen.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-toegelaten-instellingen-volkshuisvesting.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-verzekeringsmaatschappijen.xsd',
        'kvk-rpt-jaarverantwoording-2022-nlgaap-zorginstellingen.xsd',
    ]},
    DISCLOSURE_SYSTEM_NT18: {NT18_ENTRYPOINT_ROOT + e for e in [
        'kvk-rpt-jaarverantwoording-2023-ifrs-full.xsd',
        'kvk-rpt-jaarverantwoording-2023-ifrs-geconsolideerd-nlgaap-enkelvoudig.xsd',
        'kvk-rpt-jaarverantwoording-2023-ifrs-smes.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-banken.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-beleggingsentiteiten.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-cooperaties.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-cv-vof.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-fondsenwervende-organisaties-klein.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-fondsenwervende-organisaties.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-groot-verticaal.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-groot.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-klein-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-klein-verticaal-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-klein-verticaal.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-klein.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-micro-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-micro.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-middelgroot-plus.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-middelgroot-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-middelgroot-verticaal-publicatiestukken.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-middelgroot-verticaal.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-middelgroot.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-organisaties-zonder-winststreven-klein.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-organisaties-zonder-winststreven.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-pensioenfondsen.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-premiepensioeninstellingen.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-stichtingen.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-toegelaten-instellingen-volkshuisvesting.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-verzekeringsmaatschappijen.xsd',
        'kvk-rpt-jaarverantwoording-2023-nlgaap-zorginstellingen.xsd',
    ]},
}

JENV_BW2_DATA_NS = 'http://www.nltaxonomie.nl/nt16/jenv/20211208/dictionary/jenv-bw2-data'
FINANCIAL_REPORTING_PERIOD_CURRENT_START_DATE_QN = qname(f'{{{JENV_BW2_DATA_NS}}}FinancialReportingPeriodCurrentStartDate')
FINANCIAL_REPORTING_PERIOD_CURRENT_END_DATE_QN = qname(f'{{{JENV_BW2_DATA_NS}}}FinancialReportingPeriodCurrentEndDate')
FINANCIAL_REPORTING_PERIOD_PREVIOUS_START_DATE_QN = qname(f'{{{JENV_BW2_DATA_NS}}}FinancialReportingPeriodPreviousStartDate')
FINANCIAL_REPORTING_PERIOD_PREVIOUS_END_DATE_QN = qname(f'{{{JENV_BW2_DATA_NS}}}FinancialReportingPeriodPreviousEndDate')
DOCUMENTATION_ADOPTION_DATE_QN = qname(f'{{{JENV_BW2_DATA_NS}}}DocumentAdoptionDate')
DOCUMENTATION_ADOPTION_STATUS_QN = qname(f'{{{JENV_BW2_DATA_NS}}}DocumentAdoptionStatus')

KVK_I_NS = 'http://www.nltaxonomie.nl/nt16/kvk/20211208/dictionary/kvk-data'
DOCUMENT_RESUBMISSION_UNSURMOUNTABLE_INACCURACIES_QN = qname(f'{{{KVK_I_NS}}}DocumentResubmissionDueToUnsurmountableInaccuracies')
