# PREFIX = `python -c "from invenio.config import CFG_PREFIX; print CFG_PREFIX"`
# PREFIX = /opt/invenio
PREFIX = $(CFG_INVENIO_PREFIX)
LIBDIR = $(PREFIX)/lib
ETCDIR = $(PREFIX)/etc
WWWDIR = $(PREFIX)/var/www
# APACHE = `python -c "from invenio.bibtask import guess_apache_process_user; print guess_apache_process_user()"`
# APACHE = www-data
APACHE = wziolek
INSTALL = install -g $(APACHE) -m 775

scoap3dtdsdir = $(ETCDIR)/scoap3dtds
scoap3dtds_DATA = ja5_art501.zip ja5_art510.zip ja5_art520.zip si510.zip si520.zip

scoap3utils = scoap3utils.py
contrast_out = contrast_out.py
contrast_out_config = contrast_out_config.py


install:
	$(INSTALL) -d $(scoap3dtdsdir)
	$(INSTALL) -t $(scoap3dtdsdir) $(scoap3dtds_DATA)
	$(INSTALL) -t $(LIBDIR)/python/invenio $(scoap3utils)
	$(INSTALL) -t $(LIBDIR)/python/invenio $(contrast_out)
	$(INSTALL) -t $(LIBDIR)/python/invenio $(contrast_out_config)
	$(INSTALL) -t $(WWWDIR) robots.txt
	$(INSTALL) -t $(WWWDIR)/img scoap3_logo.png favicon.ico invenio_scoap3.css

install-conf:
	$(INSTALL) -t $(ETCDIR) invenio-local.conf
