namespace py weltamdraht
namespace py.twisted weltamdraht

const i16 API_VERSION = 1

struct WAD_Signature {
    1: i32 unique_id;
    2: i64 timestamp;
    3: i16 hmac;
}

struct WAD_Spatial_Location {
    1: i16 x;
    2: i16 y;
    3: i16 z;
}

service WeltamDraht{
    /**
     * Ping call - returns server version
     */
    string ping(
        1: WAD_Signature signature,
        2: string client_version
    )

    /**
     * Get Spatial Field Location - returns WAD_Spatial_Location
     */
    WAD_Spatial_Location getSpatialLocation(
        1: WAD_Signature signature
        2: i64 object_id
    )

    /**
     * Set Spatial Field Location - returns Bool
     */
    bool setSpatialLocation(
        1: WAD_Signature signature
        2: i64 object_id
    )

    /**
     * Get Objects At Field Location - returns Set
     */
    set<i64> getObjectsAtSpatialLocation(
        1: WAD_Signature signature
        2: WAD_Spatial_Location spatial_location
        3: i16 radius
    )
}
