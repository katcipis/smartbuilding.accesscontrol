package br.ufsc.identification;

import java.util.List;

import android.R;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.util.Log;
import br.ufsc.cache.AllowedPersonsCache;

public class AccessGranter {
	
	public static void grantAccess(Identification id, Context context) {
		
		try {
			List<Database.Person> allowed_persons = AllowedPersonsCache.load(context);
			
			for (Database.Person person : allowed_persons) {
				for (Database.Identification db_id : person.ids) {
					Identification person_id = IdentificationFactory.fromDatabaseId(db_id);
					if (person_id.equals(id)) {
						/* We are granting access !!! */
						openDoor();
						notifyUser (context, "Access granted: welcome " + person.name, 1, AccessGrantedActivity.class); 
						return;
					} 
		/*			else{
						closeDoor();
						//notifyUser (context, "Access not granted " + id.toString(), 1, AccessDeniedActivity.class);						
					}
				*/
			    }
			}
			
		} catch (Exception e) {
			Log.e("AccessGranter", e.toString());
			Log.e("AccessGranter", e.getMessage());
		}
		
		closeDoor();
		//notifyUser (context, "Access not granted " + id.toString(), 1); 
		notifyUser (context, "Access not granted", 1, AccessDeniedActivity.class); 
	}

	private static void notifyUser (Context context, CharSequence contentText,
		                         	int notification_id, Class<?> cls) {
		
		String ns = Context.NOTIFICATION_SERVICE;
		
		NotificationManager mNotificationManager = (NotificationManager) context.getSystemService(ns);
		
		int icon = R.drawable.status_bar_item_background;
		Notification notification = new Notification(icon, contentText, /*"Access Control Message"*/ System.currentTimeMillis());
		
		Context appContext = context.getApplicationContext();
		
		Intent notificationIntent = new Intent(context, cls);
		PendingIntent contentIntent = PendingIntent.getActivity(context, 0, notificationIntent, 0);

		notification.setLatestEventInfo(appContext, "Attempt to access room", contentText, contentIntent);
		

		mNotificationManager.notify(notification_id, notification);
		
	}

	private static native int openDoor();
	private static native int closeDoor();
	
	static{		
		System.loadLibrary("door_handler");
	}	
}
