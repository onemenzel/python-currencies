#!/usr/bin/env python
from decimal import Decimal

MONEY_CURRENCY_AED = "AED"
MONEY_CURRENCY_AFN = "AFN"
MONEY_CURRENCY_ALL = "ALL"
MONEY_CURRENCY_AMD = "AMD"
MONEY_CURRENCY_ANG = "ANG"
MONEY_CURRENCY_AOA = "AOA"
MONEY_CURRENCY_ARS = "ARS"
MONEY_CURRENCY_AUD = "AUD"
MONEY_CURRENCY_AWG = "AWG"
MONEY_CURRENCY_AZN = "AZN"
MONEY_CURRENCY_BAM = "BAM"
MONEY_CURRENCY_BBD = "BBD"
MONEY_CURRENCY_BDT = "BDT"
MONEY_CURRENCY_BGN = "BGN"
MONEY_CURRENCY_BHD = "BHD"
MONEY_CURRENCY_BND = "BND"
MONEY_CURRENCY_BOB = "BOB"
MONEY_CURRENCY_BRL = "BRL"
MONEY_CURRENCY_BSD = "BSD"
MONEY_CURRENCY_BTN = "BTN"
MONEY_CURRENCY_BWP = "BWP"
MONEY_CURRENCY_BYR = "BYR"
MONEY_CURRENCY_BZD = "BZD"
MONEY_CURRENCY_CAD = "CAD"
MONEY_CURRENCY_CHF = "CHF"
MONEY_CURRENCY_CLP = "CLP"
MONEY_CURRENCY_CNY = "CNY"
MONEY_CURRENCY_COP = "COP"
MONEY_CURRENCY_CRC = "CRC"
MONEY_CURRENCY_CZK = "CZK"
MONEY_CURRENCY_DKK = "DKK"
MONEY_CURRENCY_DOP = "DOP"
MONEY_CURRENCY_DZD = "DZD"
MONEY_CURRENCY_EGP = "EGP"
MONEY_CURRENCY_ETB = "ETB"
MONEY_CURRENCY_EUR = "EUR"
MONEY_CURRENCY_FJD = "FJD"
MONEY_CURRENCY_GBP = "GBP"
MONEY_CURRENCY_GEL = "GEL"
MONEY_CURRENCY_GHS = "GHS"
MONEY_CURRENCY_GMD = "GMD"
MONEY_CURRENCY_GTQ = "GTQ"
MONEY_CURRENCY_GYD = "GYD"
MONEY_CURRENCY_HKD = "HKD"
MONEY_CURRENCY_HNL = "HNL"
MONEY_CURRENCY_HRK = "HRK"
MONEY_CURRENCY_HUF = "HUF"
MONEY_CURRENCY_IDR = "IDR"
MONEY_CURRENCY_ILS = "ILS"
MONEY_CURRENCY_INR = "INR"
MONEY_CURRENCY_ISK = "ISK"
MONEY_CURRENCY_JEP = "JEP"
MONEY_CURRENCY_JMD = "JMD"
MONEY_CURRENCY_JOD = "JOD"
MONEY_CURRENCY_JPY = "JPY"
MONEY_CURRENCY_KES = "KES"
MONEY_CURRENCY_KGS = "KGS"
MONEY_CURRENCY_KHR = "KHR"
MONEY_CURRENCY_KRW = "KRW"
MONEY_CURRENCY_KWD = "KWD"
MONEY_CURRENCY_KYD = "KYD"
MONEY_CURRENCY_KZT = "KZT"
MONEY_CURRENCY_LBP = "LBP"
MONEY_CURRENCY_LKR = "LKR"
MONEY_CURRENCY_LTL = "LTL"
MONEY_CURRENCY_LVL = "LVL"
MONEY_CURRENCY_MAD = "MAD"
MONEY_CURRENCY_MDL = "MDL"
MONEY_CURRENCY_MGA = "MGA"
MONEY_CURRENCY_MKD = "MKD"
MONEY_CURRENCY_MMK = "MMK"
MONEY_CURRENCY_MNT = "MNT"
MONEY_CURRENCY_MOP = "MOP"
MONEY_CURRENCY_MUR = "MUR"
MONEY_CURRENCY_MVR = "MVR"
MONEY_CURRENCY_MXN = "MXN"
MONEY_CURRENCY_MYR = "MYR"
MONEY_CURRENCY_MZN = "MZN"
MONEY_CURRENCY_NAD = "NAD"
MONEY_CURRENCY_NGN = "NGN"
MONEY_CURRENCY_NIO = "NIO"
MONEY_CURRENCY_NOK = "NOK"
MONEY_CURRENCY_NPR = "NPR"
MONEY_CURRENCY_NZD = "NZD"
MONEY_CURRENCY_OMR = "OMR"
MONEY_CURRENCY_PEN = "PEN"
MONEY_CURRENCY_PGK = "PGK"
MONEY_CURRENCY_PHP = "PHP"
MONEY_CURRENCY_PKR = "PKR"
MONEY_CURRENCY_PLN = "PLN"
MONEY_CURRENCY_PYG = "PYG"
MONEY_CURRENCY_QAR = "QAR"
MONEY_CURRENCY_RON = "RON"
MONEY_CURRENCY_RSD = "RSD"
MONEY_CURRENCY_RUB = "RUB"
MONEY_CURRENCY_RWF = "RWF"
MONEY_CURRENCY_SAR = "SAR"
MONEY_CURRENCY_SCR = "SCR"
MONEY_CURRENCY_SEK = "SEK"
MONEY_CURRENCY_SGD = "SGD"
MONEY_CURRENCY_STD = "STD"
MONEY_CURRENCY_SYP = "SYP"
MONEY_CURRENCY_THB = "THB"
MONEY_CURRENCY_TND = "TND"
MONEY_CURRENCY_TRY = "TRY"
MONEY_CURRENCY_TTD = "TTD"
MONEY_CURRENCY_TWD = "TWD"
MONEY_CURRENCY_TZS = "TZS"
MONEY_CURRENCY_UAH = "UAH"
MONEY_CURRENCY_UGX = "UGX"
MONEY_CURRENCY_USD = "USD"
MONEY_CURRENCY_UYU = "UYU"
MONEY_CURRENCY_VEF = "VEF"
MONEY_CURRENCY_VND = "VND"
MONEY_CURRENCY_VUV = "VUV"
MONEY_CURRENCY_WST = "WST"
MONEY_CURRENCY_XAF = "XAF"
MONEY_CURRENCY_XBT = "XBT"
MONEY_CURRENCY_XCD = "XCD"
MONEY_CURRENCY_XOF = "XOF"
MONEY_CURRENCY_XPF = "XPF"
MONEY_CURRENCY_ZAR = "ZAR"
MONEY_CURRENCY_ZMW = "ZMW"

MONEY_FORMATS = {
    MONEY_CURRENCY_AED: {
        'money_format': 'Dhs. {amount}',
        'money_with_currency_format': 'Dhs. {amount} AED',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_AFN: {
        'money_format': 'Af {amount}',
        'money_with_currency_format': 'Af {amount} AFN',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_ALL: {
        'money_format': 'Lek {amount}',
        'money_with_currency_format': 'Lek {amount} ALL',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_AMD: {
        'money_format': '{amount} AMD',
        'money_with_currency_format': '{amount} AMD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_ANG: {
        'money_format': 'ƒ{amount}',
        'money_with_currency_format': '{amount} NAƒ',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_AOA: {
        'money_format': 'Kz{amount}',
        'money_with_currency_format': 'Kz{amount} AOA',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_ARS: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} ARS',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_AUD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} AUD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_AWG: {
        'money_format': 'Afl{amount}',
        'money_with_currency_format': 'Afl{amount} AWG',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_AZN: {
        'money_format': 'm.{amount}',
        'money_with_currency_format': 'm.{amount} AZN',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BAM: {
        'money_format': 'KM {amount}',
        'money_with_currency_format': 'KM {amount} BAM',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BBD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} Bds',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BDT: {
        'money_format': 'Tk {amount}',
        'money_with_currency_format': 'Tk {amount} BDT',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BGN: {
        'money_format': '{amount} лв',
        'money_with_currency_format': '{amount} лв BGN',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BHD: {
        'money_format': '{amount} BD',
        'money_with_currency_format': '{amount} BHD',
        'quantization': Decimal('1.000'),
    },
    MONEY_CURRENCY_BND: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} BND',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BOB: {
        'money_format': 'Bs{amount}',
        'money_with_currency_format': 'Bs{amount} BOB',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BRL: {
        'money_format': 'R$ {amount}',
        'money_with_currency_format': 'R$ {amount} BRL',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BSD: {
        'money_format': 'BS${amount}',
        'money_with_currency_format': 'BS${amount} BSD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BTN: {
        'money_format': 'Nu {amount}',
        'money_with_currency_format': 'Nu {amount} BTN',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BWP: {
        'money_format': 'P{amount}',
        'money_with_currency_format': 'P{amount} BWP',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BYR: {
        'money_format': 'Br {amount}',
        'money_with_currency_format': 'Br {amount} BYR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_BZD: {
        'money_format': 'BZ${amount}',
        'money_with_currency_format': 'BZ${amount} BZD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_CAD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} CAD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_CHF: {
        'money_format': '{amount} CHF',
        'money_with_currency_format': '{amount} CHF',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_CLP: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} CLP',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_CNY: {
        'money_format': '¥{amount}',
        'money_with_currency_format': '¥{amount} CNY',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_COP: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} COP',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_CRC: {
        'money_format': '₡ {amount}',
        'money_with_currency_format': '₡ {amount} CRC',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_CZK: {
        'money_format': '{amount} Kč',
        'money_with_currency_format': '{amount} Kč',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_DKK: {
        'money_format': '{amount}',
        'money_with_currency_format': 'kr.{amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_DOP: {
        'money_format': 'RD$ {amount}',
        'money_with_currency_format': 'RD$ {amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_DZD: {
        'money_format': 'DA {amount}',
        'money_with_currency_format': 'DA {amount} DZD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_EGP: {
        'money_format': 'LE {amount}',
        'money_with_currency_format': 'LE {amount} EGP',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_ETB: {
        'money_format': 'Br{amount}',
        'money_with_currency_format': 'Br{amount} ETB',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_EUR: {
        'money_format': '€{amount}',
        'money_with_currency_format': '€{amount} EUR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_FJD: {
        'money_format': '${amount}',
        'money_with_currency_format': 'FJ${amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_GBP: {
        'money_format': '£{amount}',
        'money_with_currency_format': '£{amount} GBP',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_GEL: {
        'money_format': '{amount} GEL',
        'money_with_currency_format': '{amount} GEL',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_GHS: {
        'money_format': 'GH₵{amount}',
        'money_with_currency_format': 'GH₵{amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_GMD: {
        'money_format': 'D {amount}',
        'money_with_currency_format': 'D {amount} GMD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_GTQ: {
        'money_format': 'Q{amount}',
        'money_with_currency_format': '{amount} GTQ',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_GYD: {
        'money_format': 'G${amount}',
        'money_with_currency_format': '${amount} GYD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_HKD: {
        'money_format': '${amount}',
        'money_with_currency_format': 'HK${amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_HNL: {
        'money_format': 'L {amount}',
        'money_with_currency_format': 'L {amount} HNL',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_HRK: {
        'money_format': '{amount} kn',
        'money_with_currency_format': '{amount} kn HRK',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_HUF: {
        'money_format': '{amount}',
        'money_with_currency_format': '{amount} Ft',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_IDR: {
        'money_format': '{amount}',
        'money_with_currency_format': 'Rp {amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_ILS: {
        'money_format': '{amount} NIS',
        'money_with_currency_format': '{amount} NIS',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_INR: {
        'money_format': '₹{amount}',
        'money_with_currency_format': '₹{amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_ISK: {
        'money_format': '{amount} kr',
        'money_with_currency_format': '{amount} kr ISK',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_JEP: {
        'money_format': '£{amount}',
        'money_with_currency_format': '£{amount} JEP',
        'quantization': None
    },
    MONEY_CURRENCY_JMD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} JMD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_JOD: {
        'money_format': '{amount} JD',
        'money_with_currency_format': '{amount} JOD',
        'quantization': Decimal('1.000'),
    },
    MONEY_CURRENCY_JPY: {
        'money_format': '¥{amount}',
        'money_with_currency_format': '¥{amount} JPY',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_KES: {
        'money_format': 'KSh{amount}',
        'money_with_currency_format': 'KSh{amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_KGS: {
        'money_format': 'лв{amount}',
        'money_with_currency_format': 'лв{amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_KHR: {
        'money_format': 'KHR{amount}',
        'money_with_currency_format': 'KHR{amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_KRW: {
        'money_format': '₩{amount}',
        'money_with_currency_format': '₩{amount} KRW',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_KWD: {
        'money_format': '{amount} KD',
        'money_with_currency_format': '{amount} KWD',
        'quantization': Decimal('1.000'),
    },
    MONEY_CURRENCY_KYD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} KYD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_KZT: {
        'money_format': '{amount} KZT',
        'money_with_currency_format': '{amount} KZT',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_LBP: {
        'money_format': 'L£{amount}',
        'money_with_currency_format': 'L£{amount} LBP',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_LKR: {
        'money_format': 'Rs {amount}',
        'money_with_currency_format': 'Rs {amount} LKR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_LTL: {
        'money_format': '{amount} Lt',
        'money_with_currency_format': '{amount} Lt',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_LVL: {
        'money_format': 'Ls {amount}',
        'money_with_currency_format': 'Ls {amount} LVL',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MAD: {
        'money_format': '{amount} dh',
        'money_with_currency_format': 'Dh {amount} MAD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MDL: {
        'money_format': '{amount} MDL',
        'money_with_currency_format': '{amount} MDL',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MGA: {
        'money_format': 'Ar {amount}',
        'money_with_currency_format': 'Ar {amount} MGA',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MKD: {
        'money_format': 'ден {amount}',
        'money_with_currency_format': 'ден {amount} MKD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MMK: {
        'money_format': 'K{amount}',
        'money_with_currency_format': 'K{amount} MMK',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MNT: {
        'money_format': '{amount} ₮',
        'money_with_currency_format': '{amount} MNT',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MOP: {
        'money_format': 'MOP${amount}',
        'money_with_currency_format': 'MOP${amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MUR: {
        'money_format': 'Rs {amount}',
        'money_with_currency_format': 'Rs {amount} MUR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MVR: {
        'money_format': 'Rf{amount}',
        'money_with_currency_format': 'Rf{amount} MRf',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MXN: {
        'money_format': '$ {amount}',
        'money_with_currency_format': '$ {amount} MXN',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MYR: {
        'money_format': 'RM{amount} MYR',
        'money_with_currency_format': 'RM{amount} MYR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_MZN: {
        'money_format': '{amount} Mt',
        'money_with_currency_format': 'Mt {amount} MZN',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_NAD: {
        'money_format': 'N${amount}',
        'money_with_currency_format': 'N${amount} NAD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_NGN: {
        'money_format': '₦{amount}',
        'money_with_currency_format': '₦{amount} NGN',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_NIO: {
        'money_format': 'C${amount}',
        'money_with_currency_format': 'C${amount} NIO',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_NOK: {
        'money_format': 'kr {amount}',
        'money_with_currency_format': 'kr {amount} NOK',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_NPR: {
        'money_format': 'Rs{amount}',
        'money_with_currency_format': 'Rs{amount} NPR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_NZD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} NZD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_OMR: {
        'money_format': '{amount} OMR',
        'money_with_currency_format': '{amount} OMR',
        'quantization': Decimal('1.000'),
    },
    MONEY_CURRENCY_PEN: {
        'money_format': 'S/. {amount}',
        'money_with_currency_format': 'S/. {amount} PEN',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_PGK: {
        'money_format': 'K {amount}',
        'money_with_currency_format': 'K {amount} PGK',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_PHP: {
        'money_format': '₱{amount}',
        'money_with_currency_format': '₱{amount} PHP',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_PKR: {
        'money_format': 'Rs.{amount}',
        'money_with_currency_format': 'Rs.{amount} PKR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_PLN: {
        'money_format': '{amount} zl',
        'money_with_currency_format': '{amount} zl PLN',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_PYG: {
        'money_format': 'Gs. {amount}',
        'money_with_currency_format': 'Gs. {amount} PYG',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_QAR: {
        'money_format': 'QAR {amount}',
        'money_with_currency_format': 'QAR {amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_RON: {
        'money_format': '{amount} lei',
        'money_with_currency_format': '{amount} lei RON',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_RSD: {
        'money_format': '{amount} RSD',
        'money_with_currency_format': '{amount} RSD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_RUB: {
        'money_format': 'руб{amount}',
        'money_with_currency_format': 'руб{amount} RUB',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_RWF: {
        'money_format': '{amount} RF',
        'money_with_currency_format': '{amount} RWF',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_SAR: {
        'money_format': '{amount} SR',
        'money_with_currency_format': '{amount} SAR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_SCR: {
        'money_format': 'Rs {amount}',
        'money_with_currency_format': 'Rs {amount} SCR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_SEK: {
        'money_format': '{amount} kr',
        'money_with_currency_format': '{amount} kr SEK',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_SGD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} SGD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_STD: {
        'money_format': 'Db {amount}',
        'money_with_currency_format': 'Db {amount} STD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_SYP: {
        'money_format': 'S£{amount}',
        'money_with_currency_format': 'S£{amount} SYP',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_THB: {
        'money_format': '{amount} ฿',
        'money_with_currency_format': '{amount} ฿ THB',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_TND: {
        'money_format': '{amount}',
        'money_with_currency_format': '{amount} DT',
        'quantization': Decimal('1.000'),
    },
    MONEY_CURRENCY_TRY: {
        'money_format': '{amount}TL',
        'money_with_currency_format': '{amount}TL',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_TTD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} TTD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_TWD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} TWD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_TZS: {
        'money_format': '{amount} TZS',
        'money_with_currency_format': '{amount} TZS',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_UAH: {
        'money_format': '₴{amount}',
        'money_with_currency_format': '₴{amount} UAH',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_UGX: {
        'money_format': 'Ush {amount}',
        'money_with_currency_format': 'Ush {amount} UGX',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_USD: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} USD',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_UYU: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount} UYU',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_VEF: {
        'money_format': 'Bs. {amount}',
        'money_with_currency_format': 'Bs. {amount} VEF',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_VND: {
        'money_format': '{amount}₫',
        'money_with_currency_format': '{amount} VND',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_VUV: {
        'money_format': '${amount}',
        'money_with_currency_format': '${amount}VT',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_WST: {
        'money_format': 'WS$ {amount}',
        'money_with_currency_format': 'WS$ {amount} WST',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_XAF: {
        'money_format': 'FCFA{amount}',
        'money_with_currency_format': 'FCFA{amount} XAF',
        'quantization': Decimal('1'),
    },
    # not a real currency
    MONEY_CURRENCY_XBT: {
        'money_format': '{amount} BTC',
        'money_with_currency_format': '{amount} BTC',
        'quantization': Decimal('1.00000000'),
    },
    MONEY_CURRENCY_XCD: {
        'money_format': '${amount}',
        'money_with_currency_format': 'EC${amount}',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_XOF: {
        'money_format': 'CFA{amount}',
        'money_with_currency_format': 'CFA{amount} XOF',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_XPF: {
        'money_format': '{amount} XPF',
        'money_with_currency_format': '{amount} XPF',
        'quantization': Decimal('1'),
    },
    MONEY_CURRENCY_ZAR: {
        'money_format': 'R {amount}',
        'money_with_currency_format': 'R {amount} ZAR',
        'quantization': Decimal('1.00'),
    },
    MONEY_CURRENCY_ZMW: {
        'money_format': 'K{amount}',
        'money_with_currency_format': 'ZMW{amount}',
        'quantization': Decimal('1.00'),
    }
}
