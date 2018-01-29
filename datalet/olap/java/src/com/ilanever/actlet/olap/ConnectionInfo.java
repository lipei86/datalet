package com.ilanever.actlet.olap;

import com.ilanever.sql.JdbcType;

/**
 * the info of connection
 * */
public class ConnectionInfo {

	/**
	 * The name of the user to log on to the JDBC database.
	 * (If your JDBC driver allows you to specify the user name in the JDBC URL, you don't need to set this property.)
	 * */
	public static String PROP_JDBCUSER = "JdbcUser";
	/**
	 * The name of the password to log on to the JDBC database.
	 * (If your JDBC driver allows you to specify the password in the JDBC URL, you don't need to set this property.)
	 * */
	public static String PROP_JDBCPASSWORD = "JdbcPassword";
	/**
	 * The URL of the catalog, an XML file which describes the schema: cubes, hierarchies, and so forth.
	 * */
	public static String PROP_CATALOG = "Catalog";
	/**
	 * An XML string representing the schema: cubes, hierarchies, and so forth.
	 * */
	public static String PROP_CATALOGCONTENT = "CatalogContent";
	/**
	 * The name of the role to adopt for access-control purposes.
	 * If not specified, the connection uses a role which has access to every object in the schema.
	 *
	 * This property can contain multiple role names separated by commas.
	 * If so, queries in the connection execute with the sum of the privileges of all of the rules;
	 * the effect is the same as running under a union role, defined using the <Union> element in the schema file.
	 * */
	public static String PROP_ROLE = "Role";


	/**
	 * construct the connection info by default
	 * */
	public ConnectionInfo() {
	}

	/**
	 * construct the connection info by parameters
	 *
	 * @param jdbcType
	 *            the type of JDBC
	 * @param server
	 *            the address of database server
	 * @param databaseName
	 *            the name of database
	 * @param jdbcUser
	 *            the user name of JDBC
	 * @param jdbcPassword
	 *            the user password of JDBC
	 * */
	public ConnectionInfo(JdbcType jdbcType, String server,
			String databaseName, String jdbcUser, String jdbcPassword) {
		this.setJdbcType(jdbcType);
		this.setServer(server);
		this.setDataBaseName(databaseName);
		this.setJdbcUser(jdbcUser);
		this.setJdbcPassword(jdbcPassword);
	}

	/**
	 * construct the connection info by parameters
	 *
	 * @param jdbcType
	 *            the type of JDBC
	 * @param server
	 *            the address of database server
	 * @param port
	 *            the port of database server
	 * @param databaseName
	 *            the name of database
	 * @param jdbcUser
	 *            the user name of JDBC
	 * @param jdbcPassword
	 *            the user password of JDBC
	 * */
	public ConnectionInfo(JdbcType jdbcType, String server, Integer port,
			String databaseName, String jdbcUser, String jdbcPassword) {
		this.setJdbcType(jdbcType);
		this.setServer(server);
		this.setPort(port);
		this.setDataBaseName(databaseName);
		this.setJdbcUser(jdbcUser);
		this.setJdbcPassword(jdbcPassword);
	}

	/**
	 * construct the connection info by parameters
	 *
	 * @param jdbcType
	 *            the type of JDBC
	 * @param jdbcDriver
	 * 			  the name of JDBC driver
	 * @param server
	 *            the address of database server
	 * @param port
	 *            the port of database server
	 * @param databaseName
	 *            the name of database
	 * @param jdbcUser
	 *            the user name of JDBC
	 * @param jdbcPassword
	 *            the user password of JDBC
	 * */
	public ConnectionInfo(JdbcType jdbcType, String jdbcDriver, String server, Integer port,
			String databaseName, String jdbcUser, String jdbcPassword) {
		this.setJdbcType(jdbcType);
		this.setJdbcDriver(jdbcDriver);
		this.setServer(server);
		this.setPort(port);
		this.setDataBaseName(databaseName);
		this.setJdbcUser(jdbcUser);
		this.setJdbcPassword(jdbcPassword);
	}

	private JdbcType jdbcType;

	public JdbcType getJdbcType() {
		return this.jdbcType;
	}

	public void setJdbcType(JdbcType type) {
		this.jdbcType = type;
	}

	private String jdbcDriver;

	public void setJdbcDriver(String driver) {
		this.jdbcDriver = driver;
	}

	public String getJdbcDriver() {
		return (this.jdbcDriver != null && !this.jdbcDriver.trim().equals("")) ? this.jdbcDriver
				: this.jdbcType.getJdbcDriver();
	}

	private String server;

	public String getServer() {
		return this.server;
	}

	public void setServer(String server) {
		this.server = server;
	}

	private Integer port = null;

	public Integer getPort() {
		return this.port = this.port == null ? this.jdbcType.getDefaultPort()
				: this.port;
	}

	public void setPort(Integer port) {
		this.port = port;
	}

	private String dbName;

	public String getDataBaseName() {
		return this.dbName;
	}

	public void setDataBaseName(String name) {
		this.dbName = name;
	}

	private String jdbcUser;

	public String getJdbcUser() {
		return this.jdbcUser;
	}

	public void setJdbcUser(String userName) {
		this.jdbcUser = userName;
	}

	private String jdbcPassword;

	public String getJdbcPassword() {
		return this.jdbcPassword;
	}

	public void setJdbcPassword(String pwd) {
		this.jdbcPassword = pwd;
	}

	/**
	 * get the URL of JDBC's connect
	 * */
	public String getJdbcUrl() {

		if(this.getServer()  == null || this.getServer().trim().length() == 0){
			throw new NullPointerException("'Server' can not be null.");
		}
		if(this.getDataBaseName() == null || this.getDataBaseName().trim().length() == 0){
			throw new NullPointerException("'DatabaseName' can not be null.");
		}
		return String.format(this.getJdbcType().getUrlFormat(),
				this.getServer(), this.getPort(), this.getDataBaseName());
	}
}
