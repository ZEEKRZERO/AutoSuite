# -*- coding: utf-8 -*-
# FlexRay configuration parameters definition, loading, saving, and conversion from python dict to c struct
import struct
from math import ceil, floor

from layers.appDataLay.constants import *



#node1
nodesend_fr_config = {

    
    # Cluster parameters, use naming convention in FLexRay spec
    'gdMinPropagationDelay': 0.4,
    'gdMaxInitializationError': 0.5,
    'gOffsetCorrectionMax': 12.0,
    'gdMacrotick': 2,
    'gPayloadLengthStatic': 32,
    'gNumberOfStaticSlots': 60,
    'gdStaticSlot': 50,
    'gdActionPointOffset': 6,
    'gNumberOfMinislots': 163,
    'gdMinislot': 6,
    'gdMiniSlotActionPointOffset': 3,
    'gdSymbolWindow': 16,
    'gdNIT': 103,
    'gOffsetCorrectionStart': 4000,
    'gdWakeupRxWindow': 301,
    'gColdStartAttempts': 10,
    'gListenNoise': 2,
    'gMaxWithoutClockCorrectionFatal': 14,
    'gMaxWithoutClockCorrectionPassive': 10,
    'gNetworkManagementVectorLength': 2,
    'gSyncFrameIDCountMax': 5,
    'gdCasRxLowMax': 91,
    'gdDynamicSlotIdlePhase': 1,
    'gdTSSTransmitter': 11,
    'gdWakeupSymbolRxIdle': 59,
    'gdWakeupSymbolRxLow': 55,
    'gdWakeupSymbolTxActive': 60,
    'gdWakeupSymbolTxIdle': 180,
    # Node parameters, use naming convention in FLexRay spec
    'pChannels': 0,
    'pWakeupChannel': 0,
    'pWakeupPattern': 63,
    'pPayloadLengthDynMax': 32,
    'pMicroPerCycle': 328000,
    'pdListenTimeout': 657200,
    'pRateCorrectionOut': 986,
    'pKeySlotId': 1,
    'pKeySlotOnlyEnabled': 0,
    'pKeySlotUsedForStartup': 1,
    'pKeySlotUsedForSync': 1,
    'pLatestTx': 155,
    'pOffsetCorrectionOut': 986,
    'pdAcceptedStartupRange': 110,
    'pAllowPassiveToActive': 0,
    'pClusterDriftDamping': 1,
    'pDecodingCorrection': 56,
    'pDelayCompensationA': 0,
    'pDelayCompensationB': 0,
    'pMacroInitialOffsetA': 7,
    'pMacroInitialOffsetB': 7,
    'pMicroInitialOffsetA': 24,
    'pMicroInitialOffsetB': 24,
    'pAllowHaltDueToClock': 1,
    'pdMaxDrift': 600,
    'CLOCK_SRC': 0,         # Protocol engine clock source
    'BIT_RATE': 0,          # Bit rate
    'SCM_EN': 0,            # Single channel mode enabled
    'LOG_STATUS_DATA': 1,   # Log protocol status data defined in FlexRay spec 9.3.1.3
    'FIFOA_EN': 0,          # Receive FIFO for channel A enabled
    'FIFOA_Depth': 0,
    'FIFOA_MIAFV': 0,
    'FIFOA_MIAFM': 0,
    'FIFOA_F0_EN': 0,
    'FIFOA_F0_MODE': 0,
    'FIFOA_F0_SID_LOWER': 0,
    'FIFOA_F0_SID_UPPER': 0,
    'FIFOA_F1_EN': 0,
    'FIFOA_F1_MODE': 0,
    'FIFOA_F1_SID_LOWER': 0,
    'FIFOA_F1_SID_UPPER': 0,
    'FIFOA_F2_EN': 0,
    'FIFOA_F2_MODE': 0,
    'FIFOA_F2_SID_LOWER': 0,
    'FIFOA_F2_SID_UPPER': 0,
    'FIFOA_F3_EN': 0,
    'FIFOA_F3_MODE': 0,
    'FIFOA_F3_SID_LOWER': 0,
    'FIFOA_F3_SID_UPPER': 0,
    'FIFOB_EN': 0,          # Receive FIFO for channel B enabled
    'FIFOB_Depth': 0,
    'FIFOB_MIAFV': 0,
    'FIFOB_MIAFM': 0,
    'FIFOB_F0_EN': 0,
    'FIFOB_F0_MODE': 0,
    'FIFOB_F0_SID_LOWER': 0,
    'FIFOB_F0_SID_UPPER': 0,
    'FIFOB_F1_EN': 0,
    'FIFOB_F1_MODE': 0,
    'FIFOB_F1_SID_LOWER': 0,
    'FIFOB_F1_SID_UPPER': 0,
    'FIFOB_F2_EN': 0,
    'FIFOB_F2_MODE': 0,
    'FIFOB_F2_SID_LOWER': 0,
    'FIFOB_F2_SID_UPPER': 0,
    'FIFOB_F3_EN': 0,
    'FIFOB_F3_MODE': 0,
    'FIFOB_F3_SID_LOWER': 0,
    'FIFOB_F3_SID_UPPER': 0,
    'RxMsgBufs': [                  # Receive frames configuration
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 2},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 3},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 4},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 5},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 6},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 7},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 8},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 9},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 10},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 11},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 12},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 13},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 14},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 15},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 16},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 17},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 18},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 19},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 20},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 21},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 22},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 23},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 24},
{'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 25},

    ],
    'TxMsgBufs': [                  # Transmit frames configuration
        {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 1,
  'PPI': 0, 'PayloadLenMax': 32},
          {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 26,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 27,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 28,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 29,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 30,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 31,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 32,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 33,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 34,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 35,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 36,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 37,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 38,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 39,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 40,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 41,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 42,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 43,
  'PPI': 0, 'PayloadLenMax': 32},

    ]
}


#node2

noderecv_fr_config = {

    
    # Cluster parameters, use naming convention in FLexRay spec
    'gdMinPropagationDelay': 0.0,
    'gdMaxInitializationError': 0.5,
    'gOffsetCorrectionMax': 12.0,
    'gdMacrotick': 2,
    'gPayloadLengthStatic': 32,
    'gNumberOfStaticSlots': 60,
    'gdStaticSlot': 50,
    'gdActionPointOffset': 6,
    'gNumberOfMinislots': 163,
    'gdMinislot': 6,
    'gdMiniSlotActionPointOffset': 3,
    'gdSymbolWindow': 16,
    'gdNIT': 103,
    'gOffsetCorrectionStart': 4000,
    'gdWakeupRxWindow': 301,
    'gColdStartAttempts': 10,
    'gListenNoise': 2,
    'gMaxWithoutClockCorrectionFatal': 14,
    'gMaxWithoutClockCorrectionPassive': 10,
    'gNetworkManagementVectorLength': 2,
    'gSyncFrameIDCountMax': 5,
    'gdCasRxLowMax': 91,
    'gdDynamicSlotIdlePhase': 1,
    'gdTSSTransmitter': 11,
    'gdWakeupSymbolRxIdle': 59,
    'gdWakeupSymbolRxLow': 55,
    'gdWakeupSymbolTxActive': 60,
    'gdWakeupSymbolTxIdle': 180,
    'nStar': 0,
    # Node parameters, use naming convention in FLexRay spec
    'pChannels': 0,
    'pWakeupChannel': 0,
    'pWakeupPattern': 63,
    'pPayloadLengthDynMax': 32,
    'pMicroPerCycle': 328000,
    'pdListenTimeout': 657200,
    'pRateCorrectionOut': 986,
    'pKeySlotId': 2,
    'pKeySlotOnlyEnabled': 0,
    'pKeySlotUsedForStartup': 1,
    'pKeySlotUsedForSync': 1,
    'pLatestTx': 155,
    'pOffsetCorrectionOut': 986,
    'pdAcceptedStartupRange': 110,
    'pAllowPassiveToActive': 0,
    'pClusterDriftDamping': 1,
    'pDecodingCorrection': 56,
    'pDelayCompensationA': 0,
    'pDelayCompensationB': 0,
    'pMacroInitialOffsetA': 7,
    'pMacroInitialOffsetB': 7,
    'pMicroInitialOffsetA': 24,
    'pMicroInitialOffsetB': 24,
    'pAllowHaltDueToClock': 1,
    'pdMaxDrift': 600,
    'CLOCK_SRC': 0,         # Protocol engine clock source
    'BIT_RATE': 0,          # Bit rate
    'SCM_EN': 0,            # Single channel mode enabled
    'LOG_STATUS_DATA': 1,   # Log protocol status data defined in FlexRay spec 9.3.1.3
    'FIFOA_EN': 0,          # Receive FIFO for channel A enabled
    'FIFOA_Depth': 0,
    'FIFOA_MIAFV': 0,
    'FIFOA_MIAFM': 0,
    'FIFOA_F0_EN': 0,
    'FIFOA_F0_MODE': 0,
    'FIFOA_F0_SID_LOWER': 0,
    'FIFOA_F0_SID_UPPER': 0,
    'FIFOA_F1_EN': 0,
    'FIFOA_F1_MODE': 0,
    'FIFOA_F1_SID_LOWER': 0,
    'FIFOA_F1_SID_UPPER': 0,
    'FIFOA_F2_EN': 0,
    'FIFOA_F2_MODE': 0,
    'FIFOA_F2_SID_LOWER': 0,
    'FIFOA_F2_SID_UPPER': 0,
    'FIFOA_F3_EN': 0,
    'FIFOA_F3_MODE': 0,
    'FIFOA_F3_SID_LOWER': 0,
    'FIFOA_F3_SID_UPPER': 0,
    'FIFOB_EN': 0,          # Receive FIFO for channel B enabled
    'FIFOB_Depth': 0,
    'FIFOB_MIAFV': 0,
    'FIFOB_MIAFM': 0,
    'FIFOB_F0_EN': 0,
    'FIFOB_F0_MODE': 0,
    'FIFOB_F0_SID_LOWER': 0,
    'FIFOB_F0_SID_UPPER': 0,
    'FIFOB_F1_EN': 0,
    'FIFOB_F1_MODE': 0,
    'FIFOB_F1_SID_LOWER': 0,
    'FIFOB_F1_SID_UPPER': 0,
    'FIFOB_F2_EN': 0,
    'FIFOB_F2_MODE': 0,
    'FIFOB_F2_SID_LOWER': 0,
    'FIFOB_F2_SID_UPPER': 0,
    'FIFOB_F3_EN': 0,
    'FIFOB_F3_MODE': 0,
    'FIFOB_F3_SID_LOWER': 0,
    'FIFOB_F3_SID_UPPER': 0,
    'RxMsgBufs': [                  # Receive frames configuration
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 1, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 26, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 27, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 28, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 29, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 30, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 31, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 32, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 33, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 34, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 35, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 36, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 37, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 38, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 39, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 40, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 41, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 42, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 43, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 44, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 45, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 46, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 47, 'PayloadLenMax': 8},
    {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'FrameId': 48, 'PayloadLenMax': 32},

    ],
    'TxMsgBufs': [                  # Transmit frames configuration
          {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 2,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 3,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 4,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 5,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 6,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 7,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 8,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 9,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 10,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 11,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 12,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 13,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 14,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 15,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 16,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 17,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 18,
  'PPI': 0, 'PayloadLenMax': 32},
            {'CCF_EN': 0, 'CCF_MASK': 0, 'CCF_VAL': 0, 'Channels': 3, 'DynPayloadLen': 0, 'FrameId': 19,
  'PPI': 0, 'PayloadLenMax': 32},

    ]
}

default_fr_config = {

    
    # Cluster parameters, use naming convention in FLexRay spec
    'gdMinPropagationDelay': 0.0,
    'gdMaxInitializationError': 0.5,
    'gOffsetCorrectionMax': 12.0,
    'gdMacrotick': 1,
    'gPayloadLengthStatic': 16,
    'gNumberOfStaticSlots': 60,
    'gdStaticSlot': 61,
    'gdActionPointOffset': 9,
    'gNumberOfMinislots': 129,
    'gdMinislot': 10,
    'gdMiniSlotActionPointOffset': 3,
    'gdSymbolWindow': 0,
    'gdNIT': 44,
    'gOffsetCorrectionStart': 4981,
    'gdWakeupRxWindow': 301,
    'gColdStartAttempts': 10,
    'gListenNoise': 2,
    'gMaxWithoutClockCorrectionFatal': 14,
    'gMaxWithoutClockCorrectionPassive': 10,
    'gNetworkManagementVectorLength': 2,
    'gSyncFrameIDCountMax': 8,
    'gdCasRxLowMax': 91,
    'gdDynamicSlotIdlePhase': 1,
    'gdTSSTransmitter': 9,
    'gdWakeupSymbolRxIdle': 59,
    'gdWakeupSymbolRxLow': 55,
    'gdWakeupSymbolTxActive': 60,
    'gdWakeupSymbolTxIdle': 180,
    # Node parameters, use naming convention in FLexRay spec
    'pChannels': 0,
    'pWakeupChannel': 0,
    'pWakeupPattern': 50,
    'pPayloadLengthDynMax': 16,
    'pMicroPerCycle': 200000,
    'pdListenTimeout': 401202,
    'pRateCorrectionOut': 601,
    'pKeySlotId': 1,
    'pKeySlotOnlyEnabled': 0,
    'pKeySlotUsedForStartup': 1,
    'pKeySlotUsedForSync': 1,
    'pLatestTx': 124,
    'pOffsetCorrectionOut': 378,
    'pdAcceptedStartupRange': 212,
    'pAllowPassiveToActive': 2,
    'pClusterDriftDamping': 2,
    'pDecodingCorrection': 48,
    'pDelayCompensationA': 0,
    'pDelayCompensationB': 0,
    'pMacroInitialOffsetA': 11,
    'pMacroInitialOffsetB': 11,
    'pMicroInitialOffsetA': 31,
    'pMicroInitialOffsetB': 31,
    'pAllowHaltDueToClock': 1,
    'pdMaxDrift': 601,
    'CLOCK_SRC': 0,         # Protocol engine clock source
    'BIT_RATE': 0,          # Bit rate
    'SCM_EN': 0,            # Single channel mode enabled
    'LOG_STATUS_DATA': 1,   # Log protocol status data defined in FlexRay spec 9.3.1.3
    'FIFOA_EN': 0,          # Receive FIFO for channel A enabled
    'FIFOA_Depth': 0,
    'FIFOA_MIAFV': 0,
    'FIFOA_MIAFM': 0,
    'FIFOA_F0_EN': 0,
    'FIFOA_F0_MODE': 0,
    'FIFOA_F0_SID_LOWER': 0,
    'FIFOA_F0_SID_UPPER': 0,
    'FIFOA_F1_EN': 0,
    'FIFOA_F1_MODE': 0,
    'FIFOA_F1_SID_LOWER': 0,
    'FIFOA_F1_SID_UPPER': 0,
    'FIFOA_F2_EN': 0,
    'FIFOA_F2_MODE': 0,
    'FIFOA_F2_SID_LOWER': 0,
    'FIFOA_F2_SID_UPPER': 0,
    'FIFOA_F3_EN': 0,
    'FIFOA_F3_MODE': 0,
    'FIFOA_F3_SID_LOWER': 0,
    'FIFOA_F3_SID_UPPER': 0,
    'FIFOB_EN': 0,          # Receive FIFO for channel B enabled
    'FIFOB_Depth': 0,
    'FIFOB_MIAFV': 0,
    'FIFOB_MIAFM': 0,
    'FIFOB_F0_EN': 0,
    'FIFOB_F0_MODE': 0,
    'FIFOB_F0_SID_LOWER': 0,
    'FIFOB_F0_SID_UPPER': 0,
    'FIFOB_F1_EN': 0,
    'FIFOB_F1_MODE': 0,
    'FIFOB_F1_SID_LOWER': 0,
    'FIFOB_F1_SID_UPPER': 0,
    'FIFOB_F2_EN': 0,
    'FIFOB_F2_MODE': 0,
    'FIFOB_F2_SID_LOWER': 0,
    'FIFOB_F2_SID_UPPER': 0,
    'FIFOB_F3_EN': 0,
    'FIFOB_F3_MODE': 0,
    'FIFOB_F3_SID_LOWER': 0,
    'FIFOB_F3_SID_UPPER': 0,
    'RxMsgBufs': [                  # Receive frames configuration
            {
            'FrameId': 0,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
        {
            'FrameId': 1,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
         {
            'FrameId': 2,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
                {
            'FrameId': 3,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
                {
            'FrameId': 4,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
                {
            'FrameId': 5,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
                {
            'FrameId': 6,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
                {
            'FrameId': 7,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
                {
            'FrameId': 8,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
                    {
            'FrameId': 9,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 10,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 11,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 20,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 62,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 58,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 14,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 28,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 15,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 23,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 11,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
            {
            'FrameId': 15,           # The slot id we are listening on
            'Channels': 1,          # The channel we are listening on
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
        },
    ],
    'TxMsgBufs': [                  # Transmit frames configuration
        {
            'FrameId': 1,           # The id of the slot which frame will be send on
            'PayloadLenMax': 8,     # Max payload length in words, for dynamic slot and DynPayloadLen=1 only
            'Channels': 1,          # The channel which frame will be send to
            'CCF_EN': 0,            # Cycle counter filter enabled
            'CCF_VAL': 0,           # Cycle counter filter value
            'CCF_MASK': 0,          # Cycle counter filter mask
            'DynPayloadLen': 0,     # Dynamic payload length enabled, for dynamic slot only
            'PPI': 0,               # Payload preempt flag
        },
    ]
}


def config_to_c_struct(config):
    r = b''
    field_names = ['gdMacrotick', 'gPayloadLengthStatic', 'gNumberOfStaticSlots', 'gdStaticSlot', 'gdActionPointOffset',
                   'gNumberOfMinislots', 'gdMinislot', 'gdMiniSlotActionPointOffset', 'gdSymbolWindow', 'gdNIT',
                   'gOffsetCorrectionStart', 'gdWakeupRxWindow', 'gColdStartAttempts', 'gListenNoise',
                   'gMaxWithoutClockCorrectionFatal', 'gMaxWithoutClockCorrectionPassive', 'gNetworkManagementVectorLength',
                   'gSyncFrameIDCountMax', 'gdCasRxLowMax', 'gdDynamicSlotIdlePhase', 'gdTSSTransmitter', 'gdWakeupSymbolRxIdle',
                   'gdWakeupSymbolRxLow', 'gdWakeupSymbolTxActive', 'gdWakeupSymbolTxIdle', 'pChannels', 'pWakeupChannel', 'pWakeupPattern',
                   'pPayloadLengthDynMax', 'pMicroPerCycle', 'pdListenTimeout', 'pRateCorrectionOut', 'pKeySlotId', 'pKeySlotOnlyEnabled',
                   'pKeySlotUsedForStartup', 'pKeySlotUsedForSync', 'pLatestTx', 'pOffsetCorrectionOut', 'pdAcceptedStartupRange',
                   'pAllowPassiveToActive', 'pClusterDriftDamping', 'pDecodingCorrection', 'pDelayCompensationA', 'pDelayCompensationB',
                   'pMacroInitialOffsetA', 'pMacroInitialOffsetB', 'pMicroInitialOffsetA', 'pMicroInitialOffsetB', 'pAllowHaltDueToClock', 'pdMaxDrift']
    for f in field_names:
        r += struct.pack('>I', config[f])
    r += struct.pack('>H', config['SCM_EN'] | (config['CLOCK_SRC'] << 1) | (config['FIFOA_EN'] << 2) | (config['FIFOB_EN'] << 3) | (config['LOG_STATUS_DATA'] << 4))
    r += struct.pack('>H', config['BIT_RATE'])
    r += struct.pack('>H', config['FIFOA_Depth'])
    r += struct.pack('>H', config['FIFOA_MIAFV'])
    r += struct.pack('>H', config['FIFOA_MIAFM'])
    r += struct.pack('>H',
        config['FIFOA_F0_EN'] | (config['FIFOA_F0_MODE'] << 1) |
        config['FIFOA_F1_EN'] | (config['FIFOA_F1_MODE'] << 1) |
        config['FIFOA_F2_EN'] | (config['FIFOA_F2_MODE'] << 1) |
        config['FIFOA_F3_EN'] | (config['FIFOA_F3_MODE'] << 1))
    r += struct.pack('>H', config['FIFOA_F0_SID_LOWER'])
    r += struct.pack('>H', config['FIFOA_F0_SID_UPPER'])
    r += struct.pack('>H', config['FIFOA_F1_SID_LOWER'])
    r += struct.pack('>H', config['FIFOA_F1_SID_UPPER'])
    r += struct.pack('>H', config['FIFOA_F2_SID_LOWER'])
    r += struct.pack('>H', config['FIFOA_F2_SID_UPPER'])
    r += struct.pack('>H', config['FIFOA_F3_SID_LOWER'])
    r += struct.pack('>H', config['FIFOA_F3_SID_UPPER'])
    r += struct.pack('>H', config['FIFOB_Depth'])
    r += struct.pack('>H', config['FIFOB_MIAFV'])
    r += struct.pack('>H', config['FIFOB_MIAFM'])
    r += struct.pack('>H',
        config['FIFOB_F0_EN'] | (config['FIFOB_F0_MODE'] << 1) |
        config['FIFOB_F1_EN'] | (config['FIFOB_F1_MODE'] << 1) |
        config['FIFOB_F2_EN'] | (config['FIFOB_F2_MODE'] << 1) |
        config['FIFOB_F3_EN'] | (config['FIFOB_F3_MODE'] << 1))
    r += struct.pack('>H', config['FIFOB_F0_SID_LOWER'])
    r += struct.pack('>H', config['FIFOB_F0_SID_UPPER'])
    r += struct.pack('>H', config['FIFOB_F1_SID_LOWER'])
    r += struct.pack('>H', config['FIFOB_F1_SID_UPPER'])
    r += struct.pack('>H', config['FIFOB_F2_SID_LOWER'])
    r += struct.pack('>H', config['FIFOB_F2_SID_UPPER'])
    r += struct.pack('>H', config['FIFOB_F3_SID_LOWER'])
    r += struct.pack('>H', config['FIFOB_F3_SID_UPPER'])
    r += struct.pack('>H', len(config['RxMsgBufs']))
    r += struct.pack('>H', len(config['TxMsgBufs']))
    for rmb in config['RxMsgBufs']:
        r += struct.pack('>I', 0 | (rmb['Channels'] << 1) |
                         (rmb['CCF_EN'] << 3) |
                         (rmb['CCF_VAL'] << 16) |
                         (rmb['CCF_MASK'] << 24))
        r += struct.pack('>H', rmb['FrameId'])
        r += struct.pack('>H', 0)
    for tmb in config['TxMsgBufs']:
        r += struct.pack('>I', 1 | (tmb['Channels'] << 1) |
                         (tmb['CCF_EN'] << 3) |
                         (tmb['PPI'] << 4) |
                         (tmb['DynPayloadLen'] << 5) |
                         (tmb['CCF_VAL'] << 16) |
                         (tmb['CCF_MASK'] << 24))
        r += struct.pack('>H', tmb['FrameId'])
        r += struct.pack('>H', tmb['PayloadLenMax'])
    return r


def map_frame_id_to_tx_msg_buf_idx(config):
    return {tmb['FrameId']: idx for (idx, tmb) in enumerate(config['TxMsgBufs'])}


def verify_config_format(config):
    missed_keys = set(default_fr_config.keys()) - set(config.keys())
    if len(config['RxMsgBufs']) == 0:
        missed_keys.add('RxMsgBufs')
    if len(missed_keys) > 0:
        return False, missed_keys
    return True, ()


'''
Verify config parameters:
    1) Parameters constraints, as defined in FlexRay spec 2.1 B.4
    2) Tx/Rx message buffers.
'''
def verify_config(config):
    result = []
    # MPC5748G Reference Manual Table 46-55
    # pdMicrotick (ns) depends on bit rate
    # config['bit_rate']: 0: 10Mbps, 1: 5Mbps, 2: 2.5Mbps, 3: 8Mbps
    pdMicrotick_values = [25.0, 25.0, 50.0, 25.0]
    pSamplesPerMicrotick_values = [2, 1, 1, 2]
    gdSampleClockPeriod_values = [12.5, 25.0, 50.0, 12.5]
    gdBit = cSamplesPerBit * (gdSampleClockPeriod_values[config['BIT_RATE']] / 1000.0)
    result.append('gdBit {} µs'.format(gdBit))
    gdBitMax = gdBit * (1 + cClockDeviationMax)
    pdMicrotick = pdMicrotick_values[config['BIT_RATE']] / 1000.0
    result.append('pdMicrotick {} µs'.format(pdMicrotick))

    # Constraint 6
    gdMacrotick_min = cMicroPerMacroNomMin * pdMicrotick
    if config['gdMacrotick'] < cMicroPerMacroNomMin * pdMicrotick:
        return False, 'gdMacrotick should be equal or greater than {}'.format(gdMacrotick_min)

    if (config['gdActionPointOffset'] <= config['gdMiniSlotActionPointOffset'] or config['gNumberOfMinislots'] == 0):
        adActionPointDifference = 0
    else:
        adActionPointDifference = config['gdActionPointOffset'] - config['gdMiniSlotActionPointOffset']
    # Constraint 18:
    gMacroPerCycle = config['gdStaticSlot'] * config['gNumberOfStaticSlots'] + adActionPointDifference + config['gdMinislot'] * config['gNumberOfMinislots'] + config['gdSymbolWindow'] + config['gdNIT']
    result.append('gMacroPerCycle {} MT'.format(gMacroPerCycle))
    # Constraint 17:
    gdCycle = gMacroPerCycle * config['gdMacrotick']
    result.append('gdCycle {} µs'.format(gdCycle))
    if gdCycle > cdCycleMax:
        return False, 'gdCycle should not be greater than {}, but we got {}'.format(cdCycleMax, gdCycle)
    result.append('gdMacrotick {} µs'.format(config['gdMacrotick']))
    # Constraint 19
    pMicroPerCycle = round(gdCycle / pdMicrotick)
    if config['pMicroPerCycle'] != pMicroPerCycle:
        return False, ('pMicroPerCycle', pMicroPerCycle)

    # Constraint 21
    gNumberOfMinislots = \
        (gMacroPerCycle - config['gdNIT'] - adActionPointDifference - config['gNumberOfStaticSlots'] * config['gdStaticSlot'] - config['gdSymbolWindow']) * 1.0 / config['gdMinislot']
    if not gNumberOfMinislots.is_integer():
        return False, 'gNumberOfMinislots should be integer'
    if config['gNumberOfMinislots'] != int(gNumberOfMinislots):
        return False, ('gNumberOfMinislots', gNumberOfMinislots)

    # Constraint 30
    max_val = ceil(config['pMicroPerCycle'] * 2 * cClockDeviationMax / (1 - cClockDeviationMax))
    if config['pdMaxDrift'] > max_val:
        return False, 'pdMaxDrift should be equal or less than {}'.format(max_val)

    # Constraint 31
    pdListenTimeout = 2 * (config['pMicroPerCycle'] + config['pdMaxDrift'])
    if config['pdListenTimeout'] != pdListenTimeout:
        return False, ('pdListenTimeout', pdListenTimeout)

    # Constraint 32
    pDecodingCorrection = \
        round(((config['gdTSSTransmitter'] + cdFSS + 0.5 * cdBSS) * cSamplesPerBit + cStrobeOffset + cVotingDelay) / pSamplesPerMicrotick_values[config['BIT_RATE']])
    if config['pDecodingCorrection'] != pDecodingCorrection:
        return False, ('pDecodingCorrection', pDecodingCorrection)

    # Constraint 39
    gdWakeupSymbolTxIdle = ceil(cdWakeupSymbolTxIdle / gdBit)
    if config['gdWakeupSymbolTxIdle'] != gdWakeupSymbolTxIdle:
        return False, ('gdWakeupSymbolTxIdle', gdWakeupSymbolTxIdle)
    # Constraint 40
    gdWakeupSymbolTxLow = ceil(cdWakeupSymbolTxLow / gdBit)
    if config['gdWakeupSymbolTxActive'] != gdWakeupSymbolTxLow:
        return False, ('gdWakeupSymbolTxActive', gdWakeupSymbolTxLow)

    rx_slot_ids = [x['FrameId'] for x in config['RxMsgBufs']]
    if len(rx_slot_ids) == 0:
        return False, 'There should be at least one Rx message buffer.'
    if len(set(rx_slot_ids)) != len(rx_slot_ids):
        return False, 'Duplicated frame id found in Rx message buffers.'

    tx_slot_ids = [x['FrameId'] for x in config['TxMsgBufs']]
    if len(set(tx_slot_ids)) != len(tx_slot_ids):
        return False, 'Duplicated frame id found in Tx message buffers.'

    same_fids = set(rx_slot_ids) & set(tx_slot_ids)
    if len(same_fids) > 0:
        return False, 'Frame ids {} found both in Tx and Rx message buffers.'.format(same_fids)

    if config['pKeySlotId'] == 0:
        return False, 'pKeySlotId should not be zero.'
    if config['pKeySlotId'] not in tx_slot_ids:
        return False, 'pKeySlotId {} not found in Tx message buffers.'.format(config['pKeySlotId'])
    if config['pKeySlotId'] in rx_slot_ids:
        return False, 'pKeySlotId {} should not be in Rx message buffers.'.format(config['pKeySlotId'])
    return True, result
