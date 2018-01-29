package com.ilanever.sql;

public enum JdbcType {
	/**
	 * Oracle database
	 * */
	Oracle("oracle.jdbc.driver.OracleDriver","jdbc:oracle:thin:@%1s:%2d:%3s",1521),
	/**
	 * ShenTong OSCAR
	 * */
	Oscar("com.oscar.Driver","jdbc:oscar://%1s:%2d/%3s",2003),
	/**
	 * Microsoft SqlServer
	 * */
	SqlServer("com.microsoft.sqlserver.jdbc.SQLServerDriver","jdbc:sqlserver://%1s:%2d;databaseName=%3s",1433),
	/**
	 * Oracle MySql Database
	 * */
	MySql("org.gjt.mm.mysql.Driver","jdbc:mysql://%1s:%2d/%3s",3306),
	/**
	 * IBM DB2
	 * */
	DB2("Com.ibm.db2.jdbc.net.DB2Driver","jdbc:db2://%1s:%2d/%3s",50000),
	/**
	 * Sybase
	 * */
	Sybase("com.sybase.jdbc2.jdbc.SybDriver","jdbc:sybase:%3s:%1s:%2d",4500),
	/**
	 * PostgreSql
	 * */
	PostgreSql("org.postgresql.Driver","jdbc:postgresql://%1s:%2d/%3s",5432);
	
	private String jdbcDriver;
	private String urlFormat;
	private Integer defaultPort;
	
	JdbcType(String jdbcDriver,String urlFormat,Integer defaultPort){
		this.jdbcDriver = jdbcDriver;
		this.urlFormat = urlFormat;
		this.defaultPort = defaultPort;
	}
	
	/**
	 *  get the driver of JDBC
	 * */
	public String getJdbcDriver(){
		return this.jdbcDriver;
	}
	
	/**
	 * get the URL format of JDBC
	 * */
	public String getUrlFormat(){
		return this.urlFormat;
	}
	
	/**
	 * get the default port of JDBC
	 * */
	public Integer getDefaultPort(){
		return this.defaultPort;
	}
}
