/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.8 */

#ifndef PB_ISPPIPELINE_PROTOCOLS_PB_H_INCLUDED
#define PB_ISPPIPELINE_PROTOCOLS_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Enum definitions */
/* Define the enumeration for image format */
typedef enum _isppipeline_ImageFormat {
    isppipeline_ImageFormat_JPG = 0,
    isppipeline_ImageFormat_RAW8 = 1,
    isppipeline_ImageFormat_RAW10 = 2,
    isppipeline_ImageFormat_RGB565 = 3,
    isppipeline_ImageFormat_RGB24 = 4 /* Additional formats can be added here */
} isppipeline_ImageFormat;

/* Struct definitions */
/* Define the capture command from the host to the device */
typedef struct _isppipeline_CaptureImageCommand {
    uint32_t width; /* Image width */
    uint32_t height; /* Image height */
    isppipeline_ImageFormat format; /* Image format type */
} isppipeline_CaptureImageCommand;

/* Define the ISP parameter read request from the host to the device */
typedef struct _isppipeline_ReadISPParametersCommand {
    char dummy_field;
} isppipeline_ReadISPParametersCommand;

/* Define BLC parameters */
typedef struct _isppipeline_BLCParameters {
    float r_offset;
    float gr_offset;
    float gb_offset;
    float b_offset;
} isppipeline_BLCParameters;

/* Define CCM parameters as a 1D array */
typedef struct _isppipeline_CCMParameters {
    bool enabled; /* Flag to enable or disable CCM */
    pb_size_t ccm_count;
    float ccm[9]; /* CCM parameters as an array of floats */
} isppipeline_CCMParameters;

typedef struct _isppipeline_GammaParameters {
    bool enabled;
    pb_size_t gamma_count;
    uint32_t gamma[16];
} isppipeline_GammaParameters;

/* Define the ISP parameter write request from the host to the device */
typedef struct _isppipeline_WriteISPParametersCommand {
    pb_size_t which_parameter;
    union {
        isppipeline_BLCParameters blc; /* BLC parameters to write */
        isppipeline_CCMParameters ccm; /* CCM parameters to write */
        isppipeline_GammaParameters gamma; /* Gamma parameters to write */
    } parameter;
} isppipeline_WriteISPParametersCommand;

/* Define ISP module parameters, including BLC and CCM */
typedef struct _isppipeline_ISPParameters {
    bool has_blc;
    isppipeline_BLCParameters blc;
    bool has_ccm;
    isppipeline_CCMParameters ccm;
    bool has_gamma;
    isppipeline_GammaParameters gamma; /* Future module parameters can be added
 OtherModuleParameters other_module = 3; */
} isppipeline_ISPParameters;

/* Define the ISP parameters response from the device to the host */
typedef struct _isppipeline_ISPParametersResponse {
    pb_callback_t status; /* Response status, e.g., "success", "error" */
    pb_callback_t message; /* Detailed information or error description */
    bool has_parameters;
    isppipeline_ISPParameters parameters; /* ISP module parameters */
} isppipeline_ISPParametersResponse;

/* Define the image response from the device to the host */
typedef struct _isppipeline_ImageResponse {
    pb_callback_t status; /* Response status, e.g., "success", "error" */
    pb_callback_t message; /* Detailed information or error description */
    pb_callback_t image_data; /* Image data transmitted as a byte array */
    uint32_t width; /* Image width */
    uint32_t height; /* Image height */
    isppipeline_ImageFormat format; /* Image format type */
} isppipeline_ImageResponse;

/* Define the data packet that can contain different types of messages */
typedef struct _isppipeline_DataPacket {
    pb_size_t which_payload;
    union {
        isppipeline_CaptureImageCommand capture_image_command;
        isppipeline_ImageResponse image_response;
        isppipeline_ReadISPParametersCommand read_isp_parameters_command;
        isppipeline_ISPParametersResponse isp_parameters_response;
        isppipeline_WriteISPParametersCommand write_isp_parameters_command;
    } payload;
} isppipeline_DataPacket;


#ifdef __cplusplus
extern "C" {
#endif

/* Helper constants for enums */
#define _isppipeline_ImageFormat_MIN isppipeline_ImageFormat_JPG
#define _isppipeline_ImageFormat_MAX isppipeline_ImageFormat_RGB24
#define _isppipeline_ImageFormat_ARRAYSIZE ((isppipeline_ImageFormat)(isppipeline_ImageFormat_RGB24+1))

#define isppipeline_CaptureImageCommand_format_ENUMTYPE isppipeline_ImageFormat








#define isppipeline_ImageResponse_format_ENUMTYPE isppipeline_ImageFormat



/* Initializer values for message structs */
#define isppipeline_CaptureImageCommand_init_default {0, 0, _isppipeline_ImageFormat_MIN}
#define isppipeline_ReadISPParametersCommand_init_default {0}
#define isppipeline_WriteISPParametersCommand_init_default {0, {isppipeline_BLCParameters_init_default}}
#define isppipeline_BLCParameters_init_default   {0, 0, 0, 0}
#define isppipeline_CCMParameters_init_default   {0, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0}}
#define isppipeline_GammaParameters_init_default {0, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}}
#define isppipeline_ISPParameters_init_default   {false, isppipeline_BLCParameters_init_default, false, isppipeline_CCMParameters_init_default, false, isppipeline_GammaParameters_init_default}
#define isppipeline_ISPParametersResponse_init_default {{{NULL}, NULL}, {{NULL}, NULL}, false, isppipeline_ISPParameters_init_default}
#define isppipeline_ImageResponse_init_default   {{{NULL}, NULL}, {{NULL}, NULL}, {{NULL}, NULL}, 0, 0, _isppipeline_ImageFormat_MIN}
#define isppipeline_DataPacket_init_default      {0, {isppipeline_CaptureImageCommand_init_default}}
#define isppipeline_CaptureImageCommand_init_zero {0, 0, _isppipeline_ImageFormat_MIN}
#define isppipeline_ReadISPParametersCommand_init_zero {0}
#define isppipeline_WriteISPParametersCommand_init_zero {0, {isppipeline_BLCParameters_init_zero}}
#define isppipeline_BLCParameters_init_zero      {0, 0, 0, 0}
#define isppipeline_CCMParameters_init_zero      {0, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0}}
#define isppipeline_GammaParameters_init_zero    {0, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}}
#define isppipeline_ISPParameters_init_zero      {false, isppipeline_BLCParameters_init_zero, false, isppipeline_CCMParameters_init_zero, false, isppipeline_GammaParameters_init_zero}
#define isppipeline_ISPParametersResponse_init_zero {{{NULL}, NULL}, {{NULL}, NULL}, false, isppipeline_ISPParameters_init_zero}
#define isppipeline_ImageResponse_init_zero      {{{NULL}, NULL}, {{NULL}, NULL}, {{NULL}, NULL}, 0, 0, _isppipeline_ImageFormat_MIN}
#define isppipeline_DataPacket_init_zero         {0, {isppipeline_CaptureImageCommand_init_zero}}

/* Field tags (for use in manual encoding/decoding) */
#define isppipeline_CaptureImageCommand_width_tag 1
#define isppipeline_CaptureImageCommand_height_tag 2
#define isppipeline_CaptureImageCommand_format_tag 3
#define isppipeline_BLCParameters_r_offset_tag   1
#define isppipeline_BLCParameters_gr_offset_tag  2
#define isppipeline_BLCParameters_gb_offset_tag  3
#define isppipeline_BLCParameters_b_offset_tag   4
#define isppipeline_CCMParameters_enabled_tag    1
#define isppipeline_CCMParameters_ccm_tag        2
#define isppipeline_GammaParameters_enabled_tag  1
#define isppipeline_GammaParameters_gamma_tag    2
#define isppipeline_WriteISPParametersCommand_blc_tag 1
#define isppipeline_WriteISPParametersCommand_ccm_tag 2
#define isppipeline_WriteISPParametersCommand_gamma_tag 3
#define isppipeline_ISPParameters_blc_tag        1
#define isppipeline_ISPParameters_ccm_tag        2
#define isppipeline_ISPParameters_gamma_tag      3
#define isppipeline_ISPParametersResponse_status_tag 1
#define isppipeline_ISPParametersResponse_message_tag 2
#define isppipeline_ISPParametersResponse_parameters_tag 3
#define isppipeline_ImageResponse_status_tag     1
#define isppipeline_ImageResponse_message_tag    2
#define isppipeline_ImageResponse_image_data_tag 3
#define isppipeline_ImageResponse_width_tag      4
#define isppipeline_ImageResponse_height_tag     5
#define isppipeline_ImageResponse_format_tag     6
#define isppipeline_DataPacket_capture_image_command_tag 1
#define isppipeline_DataPacket_image_response_tag 2
#define isppipeline_DataPacket_read_isp_parameters_command_tag 3
#define isppipeline_DataPacket_isp_parameters_response_tag 4
#define isppipeline_DataPacket_write_isp_parameters_command_tag 5

/* Struct field encoding specification for nanopb */
#define isppipeline_CaptureImageCommand_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UINT32,   width,             1) \
X(a, STATIC,   SINGULAR, UINT32,   height,            2) \
X(a, STATIC,   SINGULAR, UENUM,    format,            3)
#define isppipeline_CaptureImageCommand_CALLBACK NULL
#define isppipeline_CaptureImageCommand_DEFAULT NULL

#define isppipeline_ReadISPParametersCommand_FIELDLIST(X, a) \

#define isppipeline_ReadISPParametersCommand_CALLBACK NULL
#define isppipeline_ReadISPParametersCommand_DEFAULT NULL

#define isppipeline_WriteISPParametersCommand_FIELDLIST(X, a) \
X(a, STATIC,   ONEOF,    MESSAGE,  (parameter,blc,parameter.blc),   1) \
X(a, STATIC,   ONEOF,    MESSAGE,  (parameter,ccm,parameter.ccm),   2) \
X(a, STATIC,   ONEOF,    MESSAGE,  (parameter,gamma,parameter.gamma),   3)
#define isppipeline_WriteISPParametersCommand_CALLBACK NULL
#define isppipeline_WriteISPParametersCommand_DEFAULT NULL
#define isppipeline_WriteISPParametersCommand_parameter_blc_MSGTYPE isppipeline_BLCParameters
#define isppipeline_WriteISPParametersCommand_parameter_ccm_MSGTYPE isppipeline_CCMParameters
#define isppipeline_WriteISPParametersCommand_parameter_gamma_MSGTYPE isppipeline_GammaParameters

#define isppipeline_BLCParameters_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, FLOAT,    r_offset,          1) \
X(a, STATIC,   SINGULAR, FLOAT,    gr_offset,         2) \
X(a, STATIC,   SINGULAR, FLOAT,    gb_offset,         3) \
X(a, STATIC,   SINGULAR, FLOAT,    b_offset,          4)
#define isppipeline_BLCParameters_CALLBACK NULL
#define isppipeline_BLCParameters_DEFAULT NULL

#define isppipeline_CCMParameters_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, BOOL,     enabled,           1) \
X(a, STATIC,   REPEATED, FLOAT,    ccm,               2)
#define isppipeline_CCMParameters_CALLBACK NULL
#define isppipeline_CCMParameters_DEFAULT NULL

#define isppipeline_GammaParameters_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, BOOL,     enabled,           1) \
X(a, STATIC,   REPEATED, UINT32,   gamma,             2)
#define isppipeline_GammaParameters_CALLBACK NULL
#define isppipeline_GammaParameters_DEFAULT NULL

#define isppipeline_ISPParameters_FIELDLIST(X, a) \
X(a, STATIC,   OPTIONAL, MESSAGE,  blc,               1) \
X(a, STATIC,   OPTIONAL, MESSAGE,  ccm,               2) \
X(a, STATIC,   OPTIONAL, MESSAGE,  gamma,             3)
#define isppipeline_ISPParameters_CALLBACK NULL
#define isppipeline_ISPParameters_DEFAULT NULL
#define isppipeline_ISPParameters_blc_MSGTYPE isppipeline_BLCParameters
#define isppipeline_ISPParameters_ccm_MSGTYPE isppipeline_CCMParameters
#define isppipeline_ISPParameters_gamma_MSGTYPE isppipeline_GammaParameters

#define isppipeline_ISPParametersResponse_FIELDLIST(X, a) \
X(a, CALLBACK, SINGULAR, STRING,   status,            1) \
X(a, CALLBACK, SINGULAR, STRING,   message,           2) \
X(a, STATIC,   OPTIONAL, MESSAGE,  parameters,        3)
#define isppipeline_ISPParametersResponse_CALLBACK pb_default_field_callback
#define isppipeline_ISPParametersResponse_DEFAULT NULL
#define isppipeline_ISPParametersResponse_parameters_MSGTYPE isppipeline_ISPParameters

#define isppipeline_ImageResponse_FIELDLIST(X, a) \
X(a, CALLBACK, SINGULAR, STRING,   status,            1) \
X(a, CALLBACK, SINGULAR, STRING,   message,           2) \
X(a, CALLBACK, SINGULAR, BYTES,    image_data,        3) \
X(a, STATIC,   SINGULAR, UINT32,   width,             4) \
X(a, STATIC,   SINGULAR, UINT32,   height,            5) \
X(a, STATIC,   SINGULAR, UENUM,    format,            6)
#define isppipeline_ImageResponse_CALLBACK pb_default_field_callback
#define isppipeline_ImageResponse_DEFAULT NULL

#define isppipeline_DataPacket_FIELDLIST(X, a) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,capture_image_command,payload.capture_image_command),   1) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,image_response,payload.image_response),   2) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,read_isp_parameters_command,payload.read_isp_parameters_command),   3) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,isp_parameters_response,payload.isp_parameters_response),   4) \
X(a, STATIC,   ONEOF,    MESSAGE,  (payload,write_isp_parameters_command,payload.write_isp_parameters_command),   5)
#define isppipeline_DataPacket_CALLBACK NULL
#define isppipeline_DataPacket_DEFAULT NULL
#define isppipeline_DataPacket_payload_capture_image_command_MSGTYPE isppipeline_CaptureImageCommand
#define isppipeline_DataPacket_payload_image_response_MSGTYPE isppipeline_ImageResponse
#define isppipeline_DataPacket_payload_read_isp_parameters_command_MSGTYPE isppipeline_ReadISPParametersCommand
#define isppipeline_DataPacket_payload_isp_parameters_response_MSGTYPE isppipeline_ISPParametersResponse
#define isppipeline_DataPacket_payload_write_isp_parameters_command_MSGTYPE isppipeline_WriteISPParametersCommand

extern const pb_msgdesc_t isppipeline_CaptureImageCommand_msg;
extern const pb_msgdesc_t isppipeline_ReadISPParametersCommand_msg;
extern const pb_msgdesc_t isppipeline_WriteISPParametersCommand_msg;
extern const pb_msgdesc_t isppipeline_BLCParameters_msg;
extern const pb_msgdesc_t isppipeline_CCMParameters_msg;
extern const pb_msgdesc_t isppipeline_GammaParameters_msg;
extern const pb_msgdesc_t isppipeline_ISPParameters_msg;
extern const pb_msgdesc_t isppipeline_ISPParametersResponse_msg;
extern const pb_msgdesc_t isppipeline_ImageResponse_msg;
extern const pb_msgdesc_t isppipeline_DataPacket_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define isppipeline_CaptureImageCommand_fields &isppipeline_CaptureImageCommand_msg
#define isppipeline_ReadISPParametersCommand_fields &isppipeline_ReadISPParametersCommand_msg
#define isppipeline_WriteISPParametersCommand_fields &isppipeline_WriteISPParametersCommand_msg
#define isppipeline_BLCParameters_fields &isppipeline_BLCParameters_msg
#define isppipeline_CCMParameters_fields &isppipeline_CCMParameters_msg
#define isppipeline_GammaParameters_fields &isppipeline_GammaParameters_msg
#define isppipeline_ISPParameters_fields &isppipeline_ISPParameters_msg
#define isppipeline_ISPParametersResponse_fields &isppipeline_ISPParametersResponse_msg
#define isppipeline_ImageResponse_fields &isppipeline_ImageResponse_msg
#define isppipeline_DataPacket_fields &isppipeline_DataPacket_msg

/* Maximum encoded size of messages (where known) */
/* isppipeline_ISPParametersResponse_size depends on runtime parameters */
/* isppipeline_ImageResponse_size depends on runtime parameters */
/* isppipeline_DataPacket_size depends on runtime parameters */
#define ISPPIPELINE_PROTOCOLS_PB_H_MAX_SIZE      isppipeline_ISPParameters_size
#define isppipeline_BLCParameters_size           20
#define isppipeline_CCMParameters_size           47
#define isppipeline_CaptureImageCommand_size     14
#define isppipeline_GammaParameters_size         98
#define isppipeline_ISPParameters_size           171
#define isppipeline_ReadISPParametersCommand_size 0
#define isppipeline_WriteISPParametersCommand_size 100

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
