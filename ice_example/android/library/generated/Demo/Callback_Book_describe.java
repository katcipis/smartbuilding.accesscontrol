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
// Generated from file `Callback_Book_describe.java'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Demo;

/**
 * Get a description of the book.
 * 
 **/

public abstract class Callback_Book_describe extends Ice.TwowayCallback
{
    public abstract void response(BookDescription __ret);

    public final void __completed(Ice.AsyncResult __result)
    {
        BookPrx __proxy = (BookPrx)__result.getProxy();
        BookDescription __ret = null;
        try
        {
            __ret = __proxy.end_describe(__result);
        }
        catch(Ice.LocalException __ex)
        {
            exception(__ex);
            return;
        }
        response(__ret);
    }
}
