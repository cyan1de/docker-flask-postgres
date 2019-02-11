# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, DateTime, Index, Integer, String, Table, text
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Na(Base):
    __tablename__ = 'nas'

    id = Column(Integer, primary_key=True, server_default=text("nextval('nas_id_seq'::regclass)"))
    nasname = Column(String(128), nullable=False, index=True)
    shortname = Column(String(32), nullable=False)
    type = Column(String(30), nullable=False, server_default=text("'other'::character varying"))
    ports = Column(Integer)
    secret = Column(String(60), nullable=False)
    server = Column(String(64))
    community = Column(String(50))
    description = Column(String(200))


class Radacct(Base):
    __tablename__ = 'radacct'
    __table_args__ = (
        Index('radacct_active_user_idx', 'username', 'nasipaddress', 'acctsessionid'),
        Index('radacct_start_user_idx', 'acctstarttime', 'username')
    )

    radacctid = Column(BigInteger, primary_key=True, server_default=text("nextval('radacct_radacctid_seq'::regclass)"))
    acctsessionid = Column(String(64), nullable=False)
    acctuniqueid = Column(String(32), nullable=False, unique=True)
    username = Column(String(253))
    groupname = Column(String(253))
    realm = Column(String(64))
    nasipaddress = Column(INET, nullable=False)
    nasportid = Column(String(15))
    nasporttype = Column(String(32))
    acctstarttime = Column(DateTime(True))
    acctstoptime = Column(DateTime(True))
    acctsessiontime = Column(BigInteger)
    acctauthentic = Column(String(32))
    connectinfo_start = Column(String(50))
    connectinfo_stop = Column(String(50))
    acctinputoctets = Column(BigInteger)
    acctoutputoctets = Column(BigInteger)
    calledstationid = Column(String(50))
    callingstationid = Column(String(50))
    acctterminatecause = Column(String(32))
    servicetype = Column(String(32))
    xascendsessionsvrkey = Column(String(10))
    framedprotocol = Column(String(32))
    framedipaddress = Column(INET)
    acctstartdelay = Column(Integer)
    acctstopdelay = Column(Integer)


class Radcheck(Base):
    __tablename__ = 'radcheck'
    __table_args__ = (
        Index('radcheck_username', 'username', 'attribute'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('radcheck_id_seq'::regclass)"))
    username = Column(String(64), nullable=False, server_default=text("''::character varying"))
    attribute = Column(String(64), nullable=False, server_default=text("''::character varying"))
    op = Column(CHAR(2), nullable=False, server_default=text("'=='::bpchar"))
    value = Column(String(253), nullable=False, server_default=text("''::character varying"))


class Radgroupcheck(Base):
    __tablename__ = 'radgroupcheck'
    __table_args__ = (
        Index('radgroupcheck_groupname', 'groupname', 'attribute'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('radgroupcheck_id_seq'::regclass)"))
    groupname = Column(String(64), nullable=False, server_default=text("''::character varying"))
    attribute = Column(String(64), nullable=False, server_default=text("''::character varying"))
    op = Column(CHAR(2), nullable=False, server_default=text("'=='::bpchar"))
    value = Column(String(253), nullable=False, server_default=text("''::character varying"))


class Radgroupreply(Base):
    __tablename__ = 'radgroupreply'
    __table_args__ = (
        Index('radgroupreply_groupname', 'groupname', 'attribute'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('radgroupreply_id_seq'::regclass)"))
    groupname = Column(String(64), nullable=False, server_default=text("''::character varying"))
    attribute = Column(String(64), nullable=False, server_default=text("''::character varying"))
    op = Column(CHAR(2), nullable=False, server_default=text("'='::bpchar"))
    value = Column(String(253), nullable=False, server_default=text("''::character varying"))


class Radpostauth(Base):
    __tablename__ = 'radpostauth'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('radpostauth_id_seq'::regclass)"))
    username = Column(String(253), nullable=False)
    _pass = Column('pass', String(128))
    reply = Column(String(32))
    calledstationid = Column(String(50))
    callingstationid = Column(String(50))
    authdate = Column(DateTime(True), nullable=False, server_default=text("'2019-01-29 23:00:37.630106+03'::timestamp with time zone"))


class Radreply(Base):
    __tablename__ = 'radreply'
    __table_args__ = (
        Index('radreply_username', 'username', 'attribute'),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('radreply_id_seq'::regclass)"))
    username = Column(String(64), nullable=False, server_default=text("''::character varying"))
    attribute = Column(String(64), nullable=False, server_default=text("''::character varying"))
    op = Column(CHAR(2), nullable=False, server_default=text("'='::bpchar"))
    value = Column(String(253), nullable=False, server_default=text("''::character varying"))


t_radusergroup = Table(
    'radusergroup', metadata,
    Column('username', String(64), nullable=False, index=True, server_default=text("''::character varying")),
    Column('groupname', String(64), nullable=False, server_default=text("''::character varying")),
    Column('priority', Integer, nullable=False, server_default=text("0"))
)