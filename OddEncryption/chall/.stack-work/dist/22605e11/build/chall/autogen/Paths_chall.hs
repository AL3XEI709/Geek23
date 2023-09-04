{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -w #-}
module Paths_chall (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where


import qualified Control.Exception as Exception
import qualified Data.List as List
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude


#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir `joinFileName` name)

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath



bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath
bindir     = "D:\\GK23\\OddEncryption\\chall\\.stack-work\\install\\cb271e71\\bin"
libdir     = "D:\\GK23\\OddEncryption\\chall\\.stack-work\\install\\cb271e71\\lib\\x86_64-windows-ghc-9.4.6\\chall-0.1.0.0-Go8adG80sfv3kL01j9siw5-chall"
dynlibdir  = "D:\\GK23\\OddEncryption\\chall\\.stack-work\\install\\cb271e71\\lib\\x86_64-windows-ghc-9.4.6"
datadir    = "D:\\GK23\\OddEncryption\\chall\\.stack-work\\install\\cb271e71\\share\\x86_64-windows-ghc-9.4.6\\chall-0.1.0.0"
libexecdir = "D:\\GK23\\OddEncryption\\chall\\.stack-work\\install\\cb271e71\\libexec\\x86_64-windows-ghc-9.4.6\\chall-0.1.0.0"
sysconfdir = "D:\\GK23\\OddEncryption\\chall\\.stack-work\\install\\cb271e71\\etc"

getBinDir     = catchIO (getEnv "chall_bindir")     (\_ -> return bindir)
getLibDir     = catchIO (getEnv "chall_libdir")     (\_ -> return libdir)
getDynLibDir  = catchIO (getEnv "chall_dynlibdir")  (\_ -> return dynlibdir)
getDataDir    = catchIO (getEnv "chall_datadir")    (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "chall_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "chall_sysconfdir") (\_ -> return sysconfdir)




joinFileName :: String -> String -> FilePath
joinFileName ""  fname = fname
joinFileName "." fname = fname
joinFileName dir ""    = dir
joinFileName dir fname
  | isPathSeparator (List.last dir) = dir ++ fname
  | otherwise                       = dir ++ pathSeparator : fname

pathSeparator :: Char
pathSeparator = '\\'

isPathSeparator :: Char -> Bool
isPathSeparator c = c == '/' || c == '\\'
