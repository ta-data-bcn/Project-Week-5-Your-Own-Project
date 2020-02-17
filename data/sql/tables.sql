CREATE TABLE IF NOT EXISTS Market (
    ID INT AUTO_INCREMENT,
    date_ref DATE,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    PRIMARY KEY(ID)
);

CREATE TABLE IF NOT EXISTS Market_country (
    ID INT AUTO_INCREMENT,
    market_ID INT,
    country VARCHAR(64),
    PRIMARY KEY(ID),
    CONSTRAINT fk_market FOREIGN KEY (market_ID)
        REFERENCES Market(ID)
        ON DELETE CASCADE
);
commit;