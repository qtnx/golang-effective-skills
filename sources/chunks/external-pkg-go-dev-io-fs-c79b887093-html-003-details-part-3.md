---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/io/fs"
source_path: "sources/raw/external/pkg-go-dev-io-fs-c79b887093.html"
license_ref: ""
---

Second, if a directory's ReadDir method (see ReadDirFile) fails, WalkDir calls the function with path set to the directory's path, d set to an DirEntry describing the directory, and err set to the error from ReadDir. In this second case, the function is called twice with the path of the directory: the first call is before the directory read is attempted and has err set to nil, giving the function a chance to return SkipDir or SkipAll and avoid the ReadDir entirely. The second call is after a failed ReadDir and reports the error from ReadDir. (If ReadDir succeeds, there is no second call.)

The differences between WalkDirFunc compared to path/filepath.WalkFunc are:

- The second argument has type DirEntry instead of FileInfo.
- The function is called before reading a directory, to allow SkipDir or SkipAll to bypass the directory read entirely or skip all remaining files and directories respectively.
- If a directory read fails, the function is called a second time for that directory to report the error.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs>

- format.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/format.go>
- fs.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/fs.go>
- glob.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/glob.go>
- readdir.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/readdir.go>
- readfile.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/readfile.go>
- readlink.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/readlink.go>
- stat.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/stat.go>
- sub.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/sub.go>
- walk.go <https://cs.opensource.google/go/go/+/go1.26.3:src/io/fs/walk.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
