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
// Generated from file `InvalidCustomerException.java'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Demo;

/**
 * This exception is raised if a customer name is invalid.
 * 
 **/
public class InvalidCustomerException extends Ice.UserException
{
    public String
    ice_name()
    {
        return "Demo::InvalidCustomerException";
    }

    public void
    __write(IceInternal.BasicStream __os)
    {
        __os.writeString("::Demo::InvalidCustomerException");
        __os.startWriteSlice();
        __os.endWriteSlice();
    }

    public void
    __read(IceInternal.BasicStream __is, boolean __rid)
    {
        if(__rid)
        {
            __is.readString();
        }
        __is.startReadSlice();
        __is.endReadSlice();
    }

    public void
    __write(Ice.OutputStream __outS)
    {
        Ice.MarshalException ex = new Ice.MarshalException();
        ex.reason = "exception Demo::InvalidCustomerException was not generated with stream support";
        throw ex;
    }

    public void
    __read(Ice.InputStream __inS, boolean __rid)
    {
        Ice.MarshalException ex = new Ice.MarshalException();
        ex.reason = "exception Demo::InvalidCustomerException was not generated with stream support";
        throw ex;
    }
}
