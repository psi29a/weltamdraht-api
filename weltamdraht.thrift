namespace py weltamdraht
namespace py.twisted weltamdraht

service WeltamDraht{
    /**
     * Ping call - returns server version
     */
    string ping(
        1: string signature,
        2: i64 user_id,
        3: i64 timestamp,
        4: string client_version
    )
}
