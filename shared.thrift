namespace py shared
namespace py.twisted weltamdraht

struct SharedStruct {
  1: i32 key
  2: string value
}

service SharedService {
  SharedStruct getStruct(1: i32 key)
}
