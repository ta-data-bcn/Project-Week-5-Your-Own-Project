
CREATE TABLE IF NOT EXISTS Market (
    ID INT AUTO_INCREMENT,
    market_name VARCHAR(64),
    date_ref DATE,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    PRIMARY KEY(ID),
    CONSTRAINT u_marketDate UNIQUE(market_name, date_ref)
);

CREATE TABLE IF NOT EXISTS Market_country (
    ID INT AUTO_INCREMENT,
    market_ID INT,
    country VARCHAR(64),
    PRIMARY KEY(ID),
    CONSTRAINT fk_market FOREIGN KEY (market_ID)
        REFERENCES Market(ID)
        ON DELETE CASCADE,
    CONSTRAINT u_marketCountry UNIQUE(market_ID,country)
);
commit;