import marshal, base64
encoded_byte_code = "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dGUuY29tL3NlYXJjaC8/cT3aBkV4Y2l0ZSkCeiNodHRwczovL3d3dy5seWNvcy5jb20vd2ViL3NlYXJjaD9xPdoFTHljb3MpAnolaHR0cHM6Ly93d3cubWV0YWNyYXdsZXIuY29tL3NlYXJjaD9xPdoLTWV0YUNyYXdsZXIpAnokaHR0cHM6Ly93d3cud2ViY3Jhd2xlci5jb20vc2VhcmNoP3E92gpXZWJDcmF3bGVyKQJ6IWh0dHBzOi8vd3d3LmRvZ3BpbGUuY29tL3NlYXJjaD9xPdoHRG9ncGlsZSkCeiJodHRwczovL3NlYXJjaC5zZXpuYW0uY3ovc2VhcmNoP3E92gZTZXpuYW0pAnomaHR0cHM6Ly93d3cuc3RhcnRwYWdlLmNvbS9kby9zZWFyY2g/cT3aCVN0YXJ0cGFnZSkCeh9odHRwczovL3d3dy5xd2FudC5jb20vc2VhcmNoP3E92gVRd2FudCkCeipodHRwczovL3d3dy5zd2lzc2Nvd3MuY29tL2VuL3NlYXJjaD9xdWVyeT3aCVN3aXNzY293cykCeiBodHRwczovL3d3dy5naWJpcnUuY29tL3NlYXJjaD9xPdoGR2liaXJ1KQJ6Hmh0dHBzOi8vd3d3LmR1Y2tkdWNrZ28uY29tLz9xPXILAAAAKQJ6HGh0dHBzOi8vd3d3LmFwb3J0LnJ1L3NlYXJjaC/aBUFwb3J0KQJ6Hmh0dHBzOi8vd3d3LnJhbWJsZXIucnUvc2VhcmNoL9oHUmFtYmxlcikCehxodHRwczovL3d3dy5uaWdtYS5ydS9zZWFyY2gv2gVOaWdtYSkCehtodHRwczovL3d3dy5zYmVyLnJ1L3NlYXJjaC/aClNiZXJTZWFyY2gpICkCeidodHRwczovL3d3dy5mYWNlYm9vay5jb20vc2VhcmNoL3RvcC8/cT3aCEZhY2Vib29rKQJ6HWh0dHBzOi8vdHdpdHRlci5jb20vc2VhcmNoP3E92gdUd2l0dGVyKQJ6J2h0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vZXhwbG9yZS90YWdzL9oJSW5zdGFncmFtKQJ6HGh0dHBzOi8vd3d3LmxpbmtlZGluLmNvbS9pbi/aCExpbmtlZEluKQJ6Lmh0dHBzOi8vdmsuY29tL3NlYXJjaD9jJTVCc2VjdGlvbiU1RD1wZW9wbGUmcT3aAlZLKQJ6KGh0dHBzOi8vb2sucnUvZGs/c3QuY21kPXVzZXJTZWFyY2gmc3QucT31GgAAANCe0LTQvdC+0LrQu9Cw0YHRgdC90LjQutC4KQJ6D2h0dHBzOi8vdC5tZS9zL9oIVGVsZWdyYW0pAnotaHR0cHM6Ly93d3cueW91dHViZS5jb20vcmVzdWx0cz9zZWFyY2hfcXVlcnk92gdZb3VUdWJlKQJ6IGh0dHBzOi8vd3d3LnJlZGRpdC5jb20vc2VhcmNoP3E92gZSZWRkaXQpAnopaHR0cHM6Ly93d3cucGludGVyZXN0LmNvbS9zZWFyY2gvcGlucy8/cT3aCVBpbnRlcmVzdCkCeh5odHRwczovL3d3dy50aWt0b2suY29tL3NlYXJjaC/aBlRpa1RvaykCeh5odHRwczovL3d3dy50dW1ibHIuY29tL3NlYXJjaC/aBlR1bWJscikCeh9odHRwczovL3d3dy5teXNwYWNlLmNvbS9zZWFyY2gv2gdNeVNwYWNlKQJ6HWh0dHBzOi8vd3d3LnNuYXBjaGF0LmNvbS9hZGQv2ghTbmFwY2hhdCkCeh9odHRwczovL3d3dy5kaXNjb3JkLmNvbS9pbnZpdGUv2gdEaXNjb3JkKQJ6K2h0dHBzOi8vd3d3LmxpdmVqb3VybmFsLmNvbS91c2Vycy9zZWFyY2g/cT3aC0xpdmVKb3VybmFsKQJ6HGh0dHBzOi8vd3d3Lm1ld2UuY29tL3NlYXJjaC/aBE1lV2UpAnojaHR0cHM6Ly93d3cuZGlhc3BvcmEuY29tL2RpcmVjdG9yeS/aCERpYXNwb3JhKQJ6Mmh0dHBzOi8vd3d3Lm1hc3RvZG9uLnNvY2lhbC93ZWIvYWNjb3VudHMvc2VhcmNoP3E92ghNYXN0b2RvbikCehtodHRwczovL3d3dy5nYWIuY29tL3NlYXJjaC/aA0dhYikCeh5odHRwczovL3d3dy5wYXJsZXIuY29tL3NlYXJjaC/aBlBhcmxlcikCeiZodHRwczovL3d3dy5taW5kcy5jb20vZGlzY292ZXIvcGVvcGxlL9oFTWluZHMpAnoaaHR0cHM6Ly93d3cudGVsZWdyYW0ubWUvcy9yKAAAACkCeiBodHRwczovL3d3dy53aGF0c2FwcC5jb20vc2VhcmNoL9oIV2hhdHNBcHApAnoeaHR0cHM6Ly93d3cuc2lnbmFsLm9yZy9zZWFyY2gv2gZTaWduYWwpAnoeaHR0cHM6Ly93d3cud2lyZS5jb20vZW4vc2VhcmNo2gRXaXJlKQJ6IGh0dHBzOi8vd3d3LnZrb250YWt0ZS5ydS9zZWFyY2gvdRIAAADQktCa0L7QvdGC0LDQutGC0LUpAnokaHR0cHM6Ly93d3cub2Rub2tsYXNzbmlraS5ydS9zZWFyY2gvcicAAAApAnoeaHR0cHM6Ly93d3cubW9pa3J1Zy5ydS9zZWFyY2gvdQ8AAADQnNC+0Lkg0JrRgNGD0LMpAnomaHR0cHM6Ly93d3cubGlua2VkaW4uY29tL3NhbGVzL3NlYXJjaC96GExpbmtlZEluIFNhbGVzIE5hdmlnYXRvcikCeh9odHRwczovL3d3dy50d2l0dGVyLmNvbS9zZWFyY2gvciMAAAApAnogaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3NlYXJjaC9yIgAAACkQKQJyBwAAAHoUR29vZ2xlIFBlb3BsZSBTZWFyY2gpAvofaHR0cHM6Ly93d3cucGlwbC5jb20vc2VhcmNoLz9xPdoEUGlwbCkC+iVodHRwczovL3d3dy5zcG9rZW8uY29tL3NlYXJjaC9wZW9wbGUv2gZTcG9rZW+pAvoiaHR0cHM6Ly93d3cud2hpdGVwYWdlcy5jb20vcGVvcGxlL9oKV2hpdGVwYWdlcykC+ihodHRwczovL3d3dy50cnVlcGVvcGxlc2VhcmNoLmNvbS9wZW9wbGUv2hBUcnVlUGVvcGxlU2VhcmNoKQL6K2h0dHBzOi8vd3d3LmJlZW52ZXJpZmllZC5jb20vcGVvcGxlLXNlYXJjaC/aDEJlZW5WZXJpZmllZCkC+idodHRwczovL3d3dy5pbnRlbGl1cy5jb20vcGVvcGxlLXNlYXJjaC/aCEludGVsaXVzKQL6Imh0dHBzOi8vd3d3LnphYmFzZWFyY2guY29tL3Blb3BsZS/aClphYmFTZWFyY2gpAvohaHR0cHM6Ly93d3cuZmFzdHBlb3BsZXNlYXJjaC5jb20v2hBGYXN0UGVvcGxlU2VhcmNoKQL6GGh0dHBzOi8vd3d3LnJhZGFyaXMuY29tL9oHUmFkYXJpcykC+hhodHRwczovL3d3dy5wZWVreW91LmNvbS/aB1BlZWtZb3UpAvodaHR0cHM6Ly93d3cucGVvcGxlbG9va3VwLmNvbS/aDFBlb3BsZUxvb2t1cCkCehtodHRwczovL3d3dy5maW5kZmFtaWx5LmNvbS/aCkZpbmRGYW1pbHkpAnoeaHR0cHM6Ly93d3cuZmFtaWx5dHJlZW5vdy5jb20v2g1GYW1pbHlUcmVlTm93cj8AAAApAnoeaHR0cHM6Ly93d3cuc3Bva2VvLmNvbS9zZWFyY2gvcj4AAAApUCkCeiFodHRwczovL3d3dy5ydXNwcm9maWxlLnJ1L3NlYXJjaC/aClJ1c3Byb2ZpbGUpAnocaHR0cHM6Ly93d3cuemFrb24ucnUvc2VhcmNoL3oIWmFrb24ucnUpAnoqaHR0cHM6Ly93d3cucm9zcmVlc3RyLnJ1L3dwcy9wb3J0YWwvcGtrNS8h2glSb3NyZWVzdHIpAnoVaHR0cHM6Ly93d3cubmFsb2cucnUvehNGZWRlcmFsIFRheCBTZXJ2aWNlKQJ6HWh0dHBzOi8vd3d3LmdhcmFudC5ydS9zZWFyY2gv2gZHYXJhbnQpAnohaHR0cHM6Ly93d3cuY29uc3VsdGFudC5ydS9zZWFyY2gveg1Db25zdWx0YW50LnJ1KQJ6Gmh0dHBzOi8vd3d3Lm1vcy5ydS9zZWFyY2gvehhNb3Njb3cgR292ZXJubWVudCBQb3J0YWwpAnoaaHR0cHM6Ly93d3cuc3BiLnJ1L3NlYXJjaC96IlNhaW50IFBldGVyc2J1cmcgR292ZXJubWVudCBQb3J0YWwpAnoYaHR0cHM6Ly93d3cuZnNzcC5nb3YucnUvehhGZWRlcmFsIEJhaWxpZmZzIFNlcnZpY2UpAnolaHR0cHM6Ly93d3cuZS1rb250dXIucnUva29udHVyLWZvY3VzL3oMS29udHVyIEZvY3VzKQJ6KWh0dHBzOi8vd3d3LnNwYXJrLWludGVyZmF4LnJ1L3NlYXJjaC5odG1seg5TcGFyayBJbnRlcmZheCkCeh9odHRwczovL3d3dy5yb3NwcmF2by5ydS9zZWFyY2gv2ghSb3NQcmF2bykCeiJodHRwczovL3d3dy5yb3NtaW56ZHJhdi5ydS9zZWFyY2gvehxNaW5pc3RyeSBvZiBIZWFsdGggb2YgUnVzc2lhKQJ6HWh0dHBzOi8vd3d3LnJvc3RlYy5ydS9zZWFyY2gvehhSb3N0ZWMgU3RhdGUgQ29ycG9yYXRpb24pAno5aHR0cHM6Ly93d3cubmFsb2cucnUvcm43Ny9zZXJ2aWNlL2Zpel92X2tvbnR1ci9pbmRleC5odG1sehpGZWRlcmFsIFRheCBTZXJ2aWNlIE1vc2NvdykCeiJodHRwczovL3d3dy5tb3MucnUvZHMvcHJlZmVjdHVyZXMvehJNb3Njb3cgUHJlZmVjdHVyZXMpAnoZaHR0cHM6Ly93d3cuZ29zdXNsdWdpLnJ1L9oJR29zdXNsdWdpKQJ6G2h0dHBzOi8vd3d3Lnpha3Vwa2kuZ292LnJ1L3oSUHVibGljIFByb2N1cmVtZW50KQJ6F2h0dHBzOi8vd3d3LnJrbi5nb3YucnUv2gxSb3Nrb21uYWR6b3IpAnoWaHR0cHM6Ly93d3cuZ3Via2luLnJ1L3oRR3Via2luIFVuaXZlcnNpdHkpAnoTaHR0cHM6Ly93d3cubXN1LnJ1L3oXTW9zY293IFN0YXRlIFVuaXZlcnNpdHkpAnoUaHR0cHM6Ly93d3cuc3BidS5ydS96IVNhaW50IFBldGVyc2J1cmcgU3RhdGUgVW5pdmVyc2l0eSkCehVodHRwczovL3d3dy5tZXBoaS5ydS96JE1vc2NvdyBFbmdpbmVlcmluZyBQaHlzaWNzIEluc3RpdHV0ZSkCehNodHRwczovL3d3dy5oc2UucnUvehpIaWdoZXIgU2Nob29sIG9mIEVjb25vbWljcykCcgcAAAB6E0dvb2dsZSBQaG9uZSBTZWFyY2gpAnIMAAAAehNZYW5kZXggUGhvbmUgU2VhcmNoKQJyCQAAAHoRQmluZyBQaG9uZSBTZWFyY2gpAnI7AAAAehFQaXBsIFBob25lIFNlYXJjaCkCcj0AAAB6E1Nwb2tlbyBQaG9uZSBTZWFyY2gpAnJAAAAAehdXaGl0ZXBhZ2VzIFBob25lIFNlYXJjaCkCckIAAAB6HVRydWVQZW9wbGVTZWFyY2ggUGhvbmUgU2VhcmNoKQJyRAAAAHoZQmVlblZlcmlmaWVkIFBob25lIFNlYXJjaCkCckYAAAB6FUludGVsaXVzIFBob25lIFNlYXJjaCkCckgAAAB6F1phYmFTZWFyY2ggUGhvbmUgU2VhcmNoKQJySgAAAHodRmFzdFBlb3BsZVNlYXJjaCBQaG9uZSBTZWFyY2gpAnJMAAAAehRSYWRhcmlzIFBob25lIFNlYXJjaCkCck4AAAB6FFBlZWtZb3UgUGhvbmUgU2VhcmNoKQJyUAAAAHoZUGVvcGxlTG9va3VwIFBob25lIFNlYXJjaCkCcgcAAAB6Ekdvb2dsZSBOYW1lIFNlYXJjaCkCcgwAAAB6EllhbmRleCBOYW1lIFNlYXJjaCkCcgkAAAB6EEJpbmcgTmFtZSBTZWFyY2gpAnI7AAAAehBQaXBsIE5hbWUgU2VhcmNoKQJyPQAAAHoSU3Bva2VvIE5hbWUgU2VhcmNoKQJyQAAAAHoWV2hpdGVwYWdlcyBOYW1lIFNlYXJjaCkCckIAAAB6HFRydWVQZW9wbGVTZWFyY2ggTmFtZSBTZWFyY2gpAnJEAAAAehhCZWVuVmVyaWZpZWQgTmFtZSBTZWFyY2gpAnJGAAAAehRJbnRlbGl1cyBOYW1lIFNlYXJjaCkCckgAAAB6FlphYmFTZWFyY2ggTmFtZSBTZWFyY2gpAnJKAAAAehxGYXN0UGVvcGxlU2VhcmNoIE5hbWUgU2VhcmNoKQJyTAAAAHoTUmFkYXJpcyBOYW1lIFNlYXJjaCkCck4AAAB6E1BlZWtZb3UgTmFtZSBTZWFyY2gpAnJQAAAAehhQZW9wbGVMb29rdXAgTmFtZSBTZWFyY2gpAnIHAAAAehNHb29nbGUgRW1haWwgU2VhcmNoKQJyDAAAAHoTWWFuZGV4IEVtYWlsIFNlYXJjaCkCcgkAAAB6EUJpbmcgRW1haWwgU2VhcmNoKQJyOwAAAHoRUGlwbCBFbWFpbCBTZWFyY2gpAnI9AAAAehNTcG9rZW8gRW1haWwgU2VhcmNoKQJyQAAAAHoXV2hpdGVwYWdlcyBFbWFpbCBTZWFyY2gpAnJCAAAAeh1UcnVlUGVvcGxlU2VhcmNoIEVtYWlsIFNlYXJjaCkCckQAAAB6GUJlZW5WZXJpZmllZCBFbWFpbCBTZWFyY2gpAnJGAAAAehVJbnRlbGl1cyBFbWFpbCBTZWFyY2gpAnJIAAAAehdaYWJhU2VhcmNoIEVtYWlsIFNlYXJjaCkCckoAAAB6HUZhc3RQZW9wbGVTZWFyY2ggRW1haWwgU2VhcmNoKQJyTAAAAHoUUmFkYXJpcyBFbWFpbCBTZWFyY2gpAnJOAAAAehRQZWVrWW91IEVtYWlsIFNlYXJjaCkCclAAAAB6GVBlb3BsZUxvb2t1cCBFbWFpbCBTZWFyY2gpAnIHAAAAehVHb29nbGUgQWRkcmVzcyBTZWFyY2gpAnIMAAAAehVZYW5kZXggQWRkcmVzcyBTZWFyY2gpAnIJAAAAehNCaW5nIEFkZHJlc3MgU2VhcmNoKQJyOwAAAHoTUGlwbCBBZGRyZXNzIFNlYXJjaCkCcj0AAAB6FVNwb2tlbyBBZGRyZXNzIFNlYXJjaCkCckAAAAB6GVdoaXRlcGFnZXMgQWRkcmVzcyBTZWFyY2gpAnJCAAAAeh9UcnVlUGVvcGxlU2VhcmNoIEFkZHJlc3MgU2VhcmNoKQJyRAAAAHobQmVlblZlcmlmaWVkIEFkZHJlc3MgU2VhcmNoKQJyRgAAAHoXSW50ZWxpdXMgQWRkcmVzcyBTZWFyY2gpAnJIAAAAehlaYWJhU2VhcmNoIEFkZHJlc3MgU2VhcmNoKQJySgAAAHofRmFzdFBlb3BsZVNlYXJjaCBBZGRyZXNzIFNlYXJjaCkCckwAAAB6FlJhZGFyaXMgQWRkcmVzcyBTZWFyY2gpAnJOAAAAehZQZWVrWW91IEFkZHJlc3MgU2VhcmNoKQJyUAAAAHobUGVvcGxlTG9va3VwIEFkZHJlc3MgU2VhcmNoegpVc2VyLUFnZW50enNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM26QUAAAApAtoHaGVhZGVyc9oHdGltZW91dOnIAAAAegtodG1sLnBhcnNlctoDZGl22gFnKQHaBmNsYXNzX9oCbGnaBmJfYWxnb3oSc2VycC1pdGVtX19jb250ZW50eg1zZWFyY2gtcmVzdWx0egtwZXJzb24tY2FyZHoOcGVvcGxlLXJlc3VsdHPaAWHaBGhyZWZ6DihodHRwcz86Ly9cUysp2gJoM9oCaDLaBXRpdGxlehtWd2lDM2IgdFpFU2ZiIHIwMjVrYyBoSk52NmLaBlZ3aUMzYtoBcNoEc3BhbtoLZGVzY3JpcHRpb256CE5vIFRpdGxleg5ObyBEZXNjcmlwdGlvbnICAAAAKQTaBnNvdXJjZdoEbGlua3JnAAAAcmsAAAD6ASB1RgAAAFxiW9CQLdCv0IFdW9CwLdGP0ZFdK1xzW9CQLdCv0IFdW9CwLdGP0ZFdKyg/OlxzW9CQLdCv0IFdW9CwLdGP0ZFdKyk/XGJ6FlwrP1xkW1xkXC1cKFwpIF17OSx9XGR6M1xiW0EtWmEtejAtOS5fJSstXStAW0EtWmEtejAtOS4tXStcLltBLVp8YS16XXsyLH1cYnpvKGh0dHBzPzovLyg/Ond3d1wuKT8oPzpmYWNlYm9va3x0d2l0dGVyfGluc3RhZ3JhbXxsaW5rZWRpbnx2a3xva1wucnV8dFwubWV8eW91dHViZXx3YVwubWV8dGlrdG9rXC5jb20pL1teXFxzXSspehNAW2EtekEtWjAtOV9dezEsMTV9ehMjW2EtekEtWjAtOV9dezEsMTV9dTQAAABcYlvQkC3Qr9CwLdGPXStcc1vQkC3Qr9CwLdGPXSsoPzpcc1vQkC3Qr9CwLdGPXSspP1xidToAAABcYltBLdCv0IFdW9CwLdGP0ZFdK1xzKlvQsC3Rj9GRXSpccypb0JAt0K/QgV0/W9CwLdGP0ZFdKlxiehtcYlxkezEsMn1cLlxkezEsMn1cLlxkezR9XGJ6F1xiWzAtOV17NH1ccz9bMC05XXs2fVxidSYAAABcYltB0JAt0K/QgV17MX1bMC05XXszfVtBLdCv0IFdezIsM31cYnpQXGItP1xkezEsM31cLlxkezR9LD9ccyotP1xkezEsM31cLlxkezR9XGJ8XGItP1xkezEsM31cLlxkezR9XHMtP1xkezEsM31cLlxkezR9XGLaBW5hbWVz2gZwaG9uZXPaBmVtYWlsc9oMc29jaWFsX21lZGlh2gl1c2VybmFtZXPaCGhhc2h0YWdz2glhZGRyZXNzZXPaBmNpdGllc9oLYmlydGhfZGF0ZXPaEHBhc3Nwb3J0X251bWJlcnPaC2Nhcl9udW1iZXJz2g1nZW9fbG9jYXRpb25zdSkAAAAK0J3QsNC50LTQtdC90L3Ri9C1INGA0LXQt9GD0LvRjNGC0LDRgtGLOnUTAAAACtCY0YHRgtC+0YfQvdC40Lo6IHJsAAAAdQ8AAAAK0KHRgdGL0LvQutCwOiBybQAAAHUVAAAACtCX0LDQs9C+0LvQvtCy0L7QujogdRMAAAAK0J7Qv9C40YHQsNC90LjQtTog+gEKdSgAAAAKCtCa0LvRjtGH0LXQstCw0Y8g0LjQvdGE0L7RgNC80LDRhtC40Y86egI6IHoCLCB6C3Jlc3VsdHMudHh02gF3egV1dGYtOCkB2ghlbmNvZGluZ3UpAAAA0J3QsNC50LTQtdC90L3Ri9C1INGA0LXQt9GD0LvRjNGC0LDRgtGLOgp1KQAAAAoK0JrQu9GO0YfQtdCy0LDRjyDQuNC90YTQvtGA0LzQsNGG0LjRjzoKdT8AAADQoNC10LfRg9C70YzRgtCw0YLRiyDQsdGL0LvQuCDRgdC+0YXRgNCw0L3QtdC90Ysg0LIgcmVzdWx0cy50eHQpFdoIcmVxdWVzdHPaA2dldNoLc3RhdHVzX2NvZGVyAwAAANoEdGV4dNoIZmluZF9hbGzaBGZpbmTaAnJl2gdmaW5kYWxs2gZhcHBlbmTaCmV4Y2VwdGlvbnPaEFJlcXVlc3RFeGNlcHRpb25yBAAAANoEbGlzdNoGZXh0ZW5k2gVwcmludNoFaXRlbXPaCmNhcGl0YWxpemXaBGpvaW7aBG9wZW7aBXdyaXRlKVTaBXF1ZXJ52gdyZXN1bHRz2g5zZWFyY2hfZW5naW5lc9oPc29jaWFsX25ldHdvcmtz2hVwZW9wbGVfc2VhcmNoX2VuZ2luZXPaFnB1YmxpY19yZWNvcmRzX2VuZ2luZXPaCmVuZ2luZV91cmzaC2VuZ2luZV9uYW1l2gN1cmxyWwAAANoIcmVzcG9uc2XaBHNvdXDaDnNlYXJjaF9yZXN1bHRz2hNzZWFyY2hfcmVzdWx0c19iaW5n2hVzZWFyY2hfcmVzdWx0c195YW5kZXjaE3NlYXJjaF9yZXN1bHRzX3BpcGzaFXNlYXJjaF9yZXN1bHRzX3Nwb2tlb9oZc2VhcmNoX3Jlc3VsdHNfd2hpdGVwYWdlc9ofc2VhcmNoX3Jlc3VsdHNfdHJ1ZXBlb3BsZXNlYXJjaNobc2VhcmNoX3Jlc3VsdHNfZmFtaWx5c2VhcmNo2hdzZWFyY2hfcmVzdWx0c191c3NlYXJjaNocc2VhcmNoX3Jlc3VsdHNfZ2VuZWFsb2d5YmFua9oZc2VhcmNoX3Jlc3VsdHNfZmluZGFncmF2ZdoXc2VhcmNoX3Jlc3VsdHNfYXJjaGl2ZXPaFXNlYXJjaF9yZXN1bHRzX2NlbnN1c9occ2VhcmNoX3Jlc3VsdHNfY291cnRsaXN0ZW5lctoXc2VhcmNoX3Jlc3VsdHNfY2FzZXRleHTaF3NlYXJjaF9yZXN1bHRzX211Y2tyYWNr2hdzZWFyY2hfcmVzdWx0c196b29taW5mb9oZc2VhcmNoX3Jlc3VsdHNfY3J1bmNoYmFzZdoYc2VhcmNoX3Jlc3VsdHNfZ2xhc3Nkb29y2h1zZWFyY2hfcmVzdWx0c19saW5rZWRpbl9zYWxlc9oac2VhcmNoX3Jlc3VsdHNfeWVsbG93cGFnZXPaGHNlYXJjaF9yZXN1bHRzX2JpemFwZWRpYdoSc2VhcmNoX3Jlc3VsdHNfZG5i2hlzZWFyY2hfcmVzdWx0c19ydXNwcm9maWxl2hRzZWFyY2hfcmVzdWx0c196YWtvbtoYc2VhcmNoX3Jlc3VsdHNfcm9zcmVlc3Ry2hRzZWFyY2hfcmVzdWx0c19uYWxvZ9oVc2VhcmNoX3Jlc3VsdHNfZ2FyYW502hlzZWFyY2hfcmVzdWx0c19jb25zdWx0YW502hJzZWFyY2hfcmVzdWx0c19tb3PaEnNlYXJjaF9yZXN1bHRzX3NwYtoTc2VhcmNoX3Jlc3VsdHNfZnNzcNoWc2VhcmNoX3Jlc3VsdHNfZWtvbnR1ctoUc2VhcmNoX3Jlc3VsdHNfc3BhcmvaF3NlYXJjaF9yZXN1bHRzX3Jvc3ByYXZv2hpzZWFyY2hfcmVzdWx0c19yb3NtaW56ZHJhdtoVc2VhcmNoX3Jlc3VsdHNfcm9zdGVj2htzZWFyY2hfcmVzdWx0c19uYWxvZ19tb3Njb3faHnNlYXJjaF9yZXN1bHRzX21vc19wcmVmZWN0dXJlc9oYc2VhcmNoX3Jlc3VsdHNfZ29zdXNsdWdp2hZzZWFyY2hfcmVzdWx0c196YWt1cGtp2hJzZWFyY2hfcmVzdWx0c19ya27aFXNlYXJjaF9yZXN1bHRzX2d1YmtpbtoSc2VhcmNoX3Jlc3VsdHNfbXN12hNzZWFyY2hfcmVzdWx0c19zcGJ12hRzZWFyY2hfcmVzdWx0c19tZXBoadoSc2VhcmNoX3Jlc3VsdHNfaHNl2gZyZXN1bHTa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"
byte_code = base64.b64decode(encoded_byte_code)
code = marshal.loads(byte_code)
exec(code)
