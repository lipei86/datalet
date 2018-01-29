package com.ilanever.actlet.olap;

import java.util.Date;

import mondrian.olap.Member;

import com.ilanever.utils.DateTimeUtils;
import com.ilanever.utils.StrUtils;

public class DateMemberFormatter implements mondrian.spi.MemberFormatter {

	@Override
	public String formatMember(Member arg0) {
		String ret = null;
		String memberval = arg0.getName();
		if(!StrUtils.isNullOrEmpty(memberval)){
			Date d = DateTimeUtils.parseISODatetime(memberval);
			if(d != null){
				ret = DateTimeUtils.dateFormat.format(d);
			}else{
				ret = memberval;
			}
		}else{
			ret = memberval;
		}
		return ret;
	}

}
