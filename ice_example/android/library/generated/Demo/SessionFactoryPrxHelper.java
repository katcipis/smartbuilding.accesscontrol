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
// Generated from file `SessionFactoryPrxHelper.java'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Demo;

/**
 * Interface to create new sessions.
 * 
 **/
public final class SessionFactoryPrxHelper extends Ice.ObjectPrxHelperBase implements SessionFactoryPrx
{
    /**
     * Create a session.
     * 
     * @return A proxy to the session.
     * 
     **/
    public SessionPrx
    create()
    {
        return create(null, false);
    }

    /**
     * Create a session.
     * 
     * @param __ctx The Context map to send with the invocation.
     * @return A proxy to the session.
     * 
     **/
    public SessionPrx
    create(java.util.Map<String, String> __ctx)
    {
        return create(__ctx, true);
    }

    private SessionPrx
    create(java.util.Map<String, String> __ctx, boolean __explicitCtx)
    {
        if(__explicitCtx && __ctx == null)
        {
            __ctx = _emptyContext;
        }
        int __cnt = 0;
        while(true)
        {
            Ice._ObjectDel __delBase = null;
            try
            {
                __checkTwowayOnly("create");
                __delBase = __getDelegate(false);
                _SessionFactoryDel __del = (_SessionFactoryDel)__delBase;
                return __del.create(__ctx);
            }
            catch(IceInternal.LocalExceptionWrapper __ex)
            {
                __handleExceptionWrapper(__delBase, __ex);
            }
            catch(Ice.LocalException __ex)
            {
                __cnt = __handleException(__delBase, __ex, null, __cnt);
            }
        }
    }

    private static final String __create_name = "create";

    /**
     * Create a session.
     * 
     * @param __cb The callback object for the operation.
     **/
    public Ice.AsyncResult begin_create()
    {
        return begin_create(null, false, null);
    }

    /**
     * Create a session.
     * 
     * @param __cb The callback object for the operation.
     * @param __ctx The Context map to send with the invocation.
     **/
    public Ice.AsyncResult begin_create(java.util.Map<String, String> __ctx)
    {
        return begin_create(__ctx, true, null);
    }

    /**
     * Create a session.
     * 
     * @param __cb The callback object for the operation.
     **/
    public Ice.AsyncResult begin_create(Ice.Callback __cb)
    {
        return begin_create(null, false, __cb);
    }

    /**
     * Create a session.
     * 
     * @param __cb The callback object for the operation.
     * @param __ctx The Context map to send with the invocation.
     **/
    public Ice.AsyncResult begin_create(java.util.Map<String, String> __ctx, Ice.Callback __cb)
    {
        return begin_create(__ctx, true, __cb);
    }

    /**
     * Create a session.
     * 
     * @param __cb The callback object for the operation.
     **/
    public Ice.AsyncResult begin_create(Callback_SessionFactory_create __cb)
    {
        return begin_create(null, false, __cb);
    }

    /**
     * Create a session.
     * 
     * @param __cb The callback object for the operation.
     * @param __ctx The Context map to send with the invocation.
     **/
    public Ice.AsyncResult begin_create(java.util.Map<String, String> __ctx, Callback_SessionFactory_create __cb)
    {
        return begin_create(__ctx, true, __cb);
    }

    private Ice.AsyncResult begin_create(java.util.Map<String, String> __ctx, boolean __explicitCtx, IceInternal.CallbackBase __cb)
    {
        __checkAsyncTwowayOnly(__create_name);
        IceInternal.OutgoingAsync __result = new IceInternal.OutgoingAsync(this, __create_name, __cb);
        try
        {
            __result.__prepare(__create_name, Ice.OperationMode.Normal, __ctx, __explicitCtx);
            IceInternal.BasicStream __os = __result.__os();
            __os.endWriteEncaps();
            __result.__send(true);
        }
        catch(Ice.LocalException __ex)
        {
            __result.__exceptionAsync(__ex);
        }
        return __result;
    }

    /**
     * ice_response indicates that
     * the operation completed successfully.
     * @param __ret (return value) A proxy to the session.
     * 
     **/
    public SessionPrx end_create(Ice.AsyncResult __result)
    {
        Ice.AsyncResult.__check(__result, this, __create_name);
        if(!__result.__wait())
        {
            try
            {
                __result.__throwUserException();
            }
            catch(Ice.UserException __ex)
            {
                throw new Ice.UnknownUserException(__ex.ice_name(), __ex);
            }
        }
        SessionPrx __ret;
        IceInternal.BasicStream __is = __result.__is();
        __is.startReadEncaps();
        __ret = SessionPrxHelper.__read(__is);
        __is.endReadEncaps();
        return __ret;
    }

    /**
     * Get the value of the session timeout. Sessions are destroyed
     * if they see no activity for this period of time.
     * 
     * @return The timeout (in seconds).
     * 
     **/
    public long
    getSessionTimeout()
    {
        return getSessionTimeout(null, false);
    }

    /**
     * Get the value of the session timeout. Sessions are destroyed
     * if they see no activity for this period of time.
     * 
     * @param __ctx The Context map to send with the invocation.
     * @return The timeout (in seconds).
     * 
     **/
    public long
    getSessionTimeout(java.util.Map<String, String> __ctx)
    {
        return getSessionTimeout(__ctx, true);
    }

    private long
    getSessionTimeout(java.util.Map<String, String> __ctx, boolean __explicitCtx)
    {
        if(__explicitCtx && __ctx == null)
        {
            __ctx = _emptyContext;
        }
        int __cnt = 0;
        while(true)
        {
            Ice._ObjectDel __delBase = null;
            try
            {
                __checkTwowayOnly("getSessionTimeout");
                __delBase = __getDelegate(false);
                _SessionFactoryDel __del = (_SessionFactoryDel)__delBase;
                return __del.getSessionTimeout(__ctx);
            }
            catch(IceInternal.LocalExceptionWrapper __ex)
            {
                __cnt = __handleExceptionWrapperRelaxed(__delBase, __ex, null, __cnt);
            }
            catch(Ice.LocalException __ex)
            {
                __cnt = __handleException(__delBase, __ex, null, __cnt);
            }
        }
    }

    private static final String __getSessionTimeout_name = "getSessionTimeout";

    /**
     * Get the value of the session timeout. Sessions are destroyed
     * if they see no activity for this period of time.
     * 
     * @param __cb The callback object for the operation.
     **/
    public Ice.AsyncResult begin_getSessionTimeout()
    {
        return begin_getSessionTimeout(null, false, null);
    }

    /**
     * Get the value of the session timeout. Sessions are destroyed
     * if they see no activity for this period of time.
     * 
     * @param __cb The callback object for the operation.
     * @param __ctx The Context map to send with the invocation.
     **/
    public Ice.AsyncResult begin_getSessionTimeout(java.util.Map<String, String> __ctx)
    {
        return begin_getSessionTimeout(__ctx, true, null);
    }

    /**
     * Get the value of the session timeout. Sessions are destroyed
     * if they see no activity for this period of time.
     * 
     * @param __cb The callback object for the operation.
     **/
    public Ice.AsyncResult begin_getSessionTimeout(Ice.Callback __cb)
    {
        return begin_getSessionTimeout(null, false, __cb);
    }

    /**
     * Get the value of the session timeout. Sessions are destroyed
     * if they see no activity for this period of time.
     * 
     * @param __cb The callback object for the operation.
     * @param __ctx The Context map to send with the invocation.
     **/
    public Ice.AsyncResult begin_getSessionTimeout(java.util.Map<String, String> __ctx, Ice.Callback __cb)
    {
        return begin_getSessionTimeout(__ctx, true, __cb);
    }

    /**
     * Get the value of the session timeout. Sessions are destroyed
     * if they see no activity for this period of time.
     * 
     * @param __cb The callback object for the operation.
     **/
    public Ice.AsyncResult begin_getSessionTimeout(Callback_SessionFactory_getSessionTimeout __cb)
    {
        return begin_getSessionTimeout(null, false, __cb);
    }

    /**
     * Get the value of the session timeout. Sessions are destroyed
     * if they see no activity for this period of time.
     * 
     * @param __cb The callback object for the operation.
     * @param __ctx The Context map to send with the invocation.
     **/
    public Ice.AsyncResult begin_getSessionTimeout(java.util.Map<String, String> __ctx, Callback_SessionFactory_getSessionTimeout __cb)
    {
        return begin_getSessionTimeout(__ctx, true, __cb);
    }

    private Ice.AsyncResult begin_getSessionTimeout(java.util.Map<String, String> __ctx, boolean __explicitCtx, IceInternal.CallbackBase __cb)
    {
        __checkAsyncTwowayOnly(__getSessionTimeout_name);
        IceInternal.OutgoingAsync __result = new IceInternal.OutgoingAsync(this, __getSessionTimeout_name, __cb);
        try
        {
            __result.__prepare(__getSessionTimeout_name, Ice.OperationMode.Nonmutating, __ctx, __explicitCtx);
            IceInternal.BasicStream __os = __result.__os();
            __os.endWriteEncaps();
            __result.__send(true);
        }
        catch(Ice.LocalException __ex)
        {
            __result.__exceptionAsync(__ex);
        }
        return __result;
    }

    /**
     * ice_response indicates that
     * the operation completed successfully.
     * @param __ret (return value) The timeout (in seconds).
     * 
     **/
    public long end_getSessionTimeout(Ice.AsyncResult __result)
    {
        Ice.AsyncResult.__check(__result, this, __getSessionTimeout_name);
        if(!__result.__wait())
        {
            try
            {
                __result.__throwUserException();
            }
            catch(Ice.UserException __ex)
            {
                throw new Ice.UnknownUserException(__ex.ice_name(), __ex);
            }
        }
        long __ret;
        IceInternal.BasicStream __is = __result.__is();
        __is.startReadEncaps();
        __ret = __is.readLong();
        __is.endReadEncaps();
        return __ret;
    }

    public static SessionFactoryPrx
    checkedCast(Ice.ObjectPrx __obj)
    {
        SessionFactoryPrx __d = null;
        if(__obj != null)
        {
            try
            {
                __d = (SessionFactoryPrx)__obj;
            }
            catch(ClassCastException ex)
            {
                if(__obj.ice_isA(ice_staticId()))
                {
                    SessionFactoryPrxHelper __h = new SessionFactoryPrxHelper();
                    __h.__copyFrom(__obj);
                    __d = __h;
                }
            }
        }
        return __d;
    }

    public static SessionFactoryPrx
    checkedCast(Ice.ObjectPrx __obj, java.util.Map<String, String> __ctx)
    {
        SessionFactoryPrx __d = null;
        if(__obj != null)
        {
            try
            {
                __d = (SessionFactoryPrx)__obj;
            }
            catch(ClassCastException ex)
            {
                if(__obj.ice_isA(ice_staticId(), __ctx))
                {
                    SessionFactoryPrxHelper __h = new SessionFactoryPrxHelper();
                    __h.__copyFrom(__obj);
                    __d = __h;
                }
            }
        }
        return __d;
    }

    public static SessionFactoryPrx
    checkedCast(Ice.ObjectPrx __obj, String __facet)
    {
        SessionFactoryPrx __d = null;
        if(__obj != null)
        {
            Ice.ObjectPrx __bb = __obj.ice_facet(__facet);
            try
            {
                if(__bb.ice_isA(ice_staticId()))
                {
                    SessionFactoryPrxHelper __h = new SessionFactoryPrxHelper();
                    __h.__copyFrom(__bb);
                    __d = __h;
                }
            }
            catch(Ice.FacetNotExistException ex)
            {
            }
        }
        return __d;
    }

    public static SessionFactoryPrx
    checkedCast(Ice.ObjectPrx __obj, String __facet, java.util.Map<String, String> __ctx)
    {
        SessionFactoryPrx __d = null;
        if(__obj != null)
        {
            Ice.ObjectPrx __bb = __obj.ice_facet(__facet);
            try
            {
                if(__bb.ice_isA(ice_staticId(), __ctx))
                {
                    SessionFactoryPrxHelper __h = new SessionFactoryPrxHelper();
                    __h.__copyFrom(__bb);
                    __d = __h;
                }
            }
            catch(Ice.FacetNotExistException ex)
            {
            }
        }
        return __d;
    }

    public static SessionFactoryPrx
    uncheckedCast(Ice.ObjectPrx __obj)
    {
        SessionFactoryPrx __d = null;
        if(__obj != null)
        {
            try
            {
                __d = (SessionFactoryPrx)__obj;
            }
            catch(ClassCastException ex)
            {
                SessionFactoryPrxHelper __h = new SessionFactoryPrxHelper();
                __h.__copyFrom(__obj);
                __d = __h;
            }
        }
        return __d;
    }

    public static SessionFactoryPrx
    uncheckedCast(Ice.ObjectPrx __obj, String __facet)
    {
        SessionFactoryPrx __d = null;
        if(__obj != null)
        {
            Ice.ObjectPrx __bb = __obj.ice_facet(__facet);
            SessionFactoryPrxHelper __h = new SessionFactoryPrxHelper();
            __h.__copyFrom(__bb);
            __d = __h;
        }
        return __d;
    }

    public static final String[] __ids =
    {
        "::Demo::SessionFactory",
        "::Ice::Object"
    };

    public static String
    ice_staticId()
    {
        return __ids[0];
    }

    protected Ice._ObjectDelM
    __createDelegateM()
    {
        return new _SessionFactoryDelM();
    }

    protected Ice._ObjectDelD
    __createDelegateD()
    {
        return new _SessionFactoryDelD();
    }

    public static void
    __write(IceInternal.BasicStream __os, SessionFactoryPrx v)
    {
        __os.writeProxy(v);
    }

    public static SessionFactoryPrx
    __read(IceInternal.BasicStream __is)
    {
        Ice.ObjectPrx proxy = __is.readProxy();
        if(proxy != null)
        {
            SessionFactoryPrxHelper result = new SessionFactoryPrxHelper();
            result.__copyFrom(proxy);
            return result;
        }
        return null;
    }
}