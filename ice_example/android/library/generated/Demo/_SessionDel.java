// **********************************************************************
//
// Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.4.2
//
// <auto-generated>
//
// Generated from file `_SessionDel.java'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Demo;

public interface _SessionDel extends Ice._ObjectDel
{
    LibraryPrx getLibrary(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void refresh(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void destroy(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;
}
