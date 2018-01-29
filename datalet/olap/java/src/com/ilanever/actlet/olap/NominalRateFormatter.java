package com.ilanever.actlet.olap;

import com.ilanever.utils.NumericUtils;
import com.ilanever.utils.StrUtils;

import mondrian.olap.Member;

public class NominalRateFormatter implements mondrian.spi.MemberFormatter {

	@Override
	public String formatMember(Member arg0) {
		String ret = null;
		String memberval = arg0.getName();
		if(!StrUtils.isNullOrEmpty(memberval)){
			Double d = NumericUtils.parseDouble(memberval);
			if(d != null){
				ret = NumericUtils.DECIMAL_BASIC_FORMATTER.format(d);
			} else {
				ret = memberval;
			}
		}
		return ret;
	}

}
