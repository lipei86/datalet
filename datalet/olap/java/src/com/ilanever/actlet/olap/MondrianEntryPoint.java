package com.ilanever.actlet.olap;

import py4j.GatewayServer;

import org.olap4j.CellSet;
import org.olap4j.OlapConnection;

public class MondrianEntryPoint {

	public String ping(String msg){
		return "your msg:" + msg;
	}

	public CellSet query_by_mdx(String olapDriver, String olapUrl, String olapCatalog, String olapMdx
		, String dbDriver, String dbUsername, String dbUserpwd) throws Exception {
		System.out.println("Execute MDX: " + olapMdx);
		CellSet cellSet = null;
		try{
			Class.forName(dbDriver);
			OlapConnection olapConn = OlapUtils.getOlapConnection(olapDriver, olapUrl, dbUsername, dbUserpwd, olapCatalog);
			cellSet = OlapUtils.query(olapConn, olapMdx);
			System.out.println("Got mdx query result.");
			return cellSet;
		} catch(Exception e){
			System.out.println(e);
		}
		return cellSet;
	}

	public static void main(String[] args){
		int port = 25333;
		MondrianEntryPoint ep = new MondrianEntryPoint();
		GatewayServer server = new GatewayServer(ep, port);
		server.start();
		System.out.println("GatewayServer started, Listening on port: " + port);
	}
}
