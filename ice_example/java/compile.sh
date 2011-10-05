mkdir -p classes
javac -d classes -classpath classes:/opt/Ice-3.4.2/lib/Ice.jar Server.java PrinterI.java generated/Demo/*.java
