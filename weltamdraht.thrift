namespace py weltamdraht
namespace py.twisted weltamdraht

const i32 API_VERSION = 1

struct WAD_Signature {
    1: i32 unique_id;
    2: i64 timestamp;
    3: i16 hmac;
}

service WeltamDraht{
    /**
     * Ping call - returns server version
     */
    string ping(
        1: WAD_Signature signature,
        2: string client_version
    )
}
