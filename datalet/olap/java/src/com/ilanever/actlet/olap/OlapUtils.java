package com.ilanever.actlet.olap;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

import org.olap4j.CellSet;
import org.olap4j.OlapConnection;
import org.olap4j.OlapException;
import org.olap4j.OlapStatement;

public class OlapUtils {

	public static OlapConnection getOlapConnection(String olapDriver, String url,
			Properties props) throws OlapException {
		OlapConnection olapConn = null;
		try {
			Class.forName(olapDriver);
			if (props == null) {
				props = new Properties();
			}
			Connection conn = DriverManager.getConnection(url, props);
			olapConn = conn.unwrap(OlapConnection.class);
		} catch (ClassNotFoundException e) {
			throw new OlapException(e.getMessage(), e);
		} catch (SQLException e) {
			throw new OlapException(e.getMessage(), e);
		}
		return olapConn;
	}

	public static OlapConnection getOlapConnection(String olapDriver, String url,
			String userName, String password, String catalog)
			throws OlapException {
		Properties props = new Properties();
		props.put(ConnectionInfo.PROP_JDBCUSER, userName);
		props.put(ConnectionInfo.PROP_JDBCPASSWORD, password);
		props.put(ConnectionInfo.PROP_CATALOG, catalog);
		return getOlapConnection(olapDriver, url, props);
	}

	public static CellSet query(OlapConnection conn, String mdx)
			throws OlapException {
		CellSet cellSet = null;
		try {
			OlapStatement smt = conn.createStatement();
			cellSet = smt.executeOlapQuery(mdx);
		} catch (OlapException e) {
			throw new OlapException(e.getMessage(), e);
		}
		return cellSet;
	}
}
