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
// Generated from file `_BookDel.java'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Demo;

public interface _BookDel extends Ice._ObjectDel
{
    BookDescription describe(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void setTitle(String title, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void setAuthors(java.util.List<String> authors, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void rentBook(String name, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper,
               BookRentedException,
               InvalidCustomerException;

    String getRenter(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper,
               BookNotRentedException;

    void returnBook(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper,
               BookNotRentedException;

    void destroy(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;
}