--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-08-20 16:55:20

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 16580)
-- Name: administrador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.administrador (
    id_adm serial NOT NULL,
    nome character varying,
    contato character varying,
    login character varying,
    senha character varying,
    endereco character varying,
    data_inicio_adm date
);


ALTER TABLE public.administrador OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16573)
-- Name: equipamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipamento (
    id_equipamento serial NOT NULL,
    nome character varying,
    qtd_estoque integer,
    tipo character varying
);


ALTER TABLE public.equipamento OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16655)
-- Name: heroi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.heroi (
    id_super_heroi bigint NOT NULL,
    disponibilidade character varying,
    contato character varying
);


ALTER TABLE public.heroi OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16601)
-- Name: missao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao (
    id_missao serial NOT NULL,
    descricao character varying,
    data date,
    status character varying,
    local character varying,
    rank character varying,
    id_adm bigint NOT NULL
);


ALTER TABLE public.missao OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16613)
-- Name: missao_equipamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao_equipamento (
    id_missao bigint NOT NULL,
    id_equipamento bigint NOT NULL,
    quantidade integer
);


ALTER TABLE public.missao_equipamento OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16679)
-- Name: missao_heroi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao_heroi (
    id_super_heroi bigint NOT NULL,
    id_missao bigint NOT NULL
);


ALTER TABLE public.missao_heroi OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16694)
-- Name: missao_vilao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao_vilao (
    id_missao bigint NOT NULL,
    id_super_vilao bigint NOT NULL
);


ALTER TABLE public.missao_vilao OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16594)
-- Name: super; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.super (
    id_super serial NOT NULL,
    nome character varying,
    descricao character varying,
    status character varying,
    rank character varying,
    fraqueza character varying,
    arqui_inimigo character varying
);


ALTER TABLE public.super OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16643)
-- Name: super_habilidade; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.super_habilidade (
    id_super bigint NOT NULL,
    classe character varying NOT NULL,
    poder character varying NOT NULL
);


ALTER TABLE public.super_habilidade OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16628)
-- Name: super_tipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.super_tipo (
    id_super bigint NOT NULL,
    id_tipo bigint NOT NULL
);


ALTER TABLE public.super_tipo OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16587)
-- Name: tipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo (
    id_tipo serial NOT NULL,
    nome character varying,
    descricao character varying
);


ALTER TABLE public.tipo OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16667)
-- Name: vilao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vilao (
    id_super_vilao bigint NOT NULL,
    situacao character varying
);


ALTER TABLE public.vilao OWNER TO postgres;

--
-- TOC entry 4911 (class 0 OID 16580)
-- Dependencies: 216
-- Data for Name: administrador; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.administrador (id_adm, nome, contato, login, senha, endereco, data_inicio_adm) FROM stdin;
\.


--
-- TOC entry 4910 (class 0 OID 16573)
-- Dependencies: 215
-- Data for Name: equipamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.equipamento (id_equipamento, nome, qtd_estoque, tipo) FROM stdin;
\.


--
-- TOC entry 4918 (class 0 OID 16655)
-- Dependencies: 223
-- Data for Name: heroi; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.heroi (id_super_heroi, disponibilidade, contato) FROM stdin;
\.


--
-- TOC entry 4914 (class 0 OID 16601)
-- Dependencies: 219
-- Data for Name: missao; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.missao (id_missao, descricao, data, status, local, rank, id_adm) FROM stdin;
\.


--
-- TOC entry 4915 (class 0 OID 16613)
-- Dependencies: 220
-- Data for Name: missao_equipamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.missao_equipamento (id_missao, id_equipamento, quantidade) FROM stdin;
\.


--
-- TOC entry 4920 (class 0 OID 16679)
-- Dependencies: 225
-- Data for Name: missao_heroi; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.missao_heroi (id_super_heroi, id_missao) FROM stdin;
\.


--
-- TOC entry 4921 (class 0 OID 16694)
-- Dependencies: 226
-- Data for Name: missao_vilao; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.missao_vilao (id_missao, id_super_vilao) FROM stdin;
\.


--
-- TOC entry 4913 (class 0 OID 16594)
-- Dependencies: 218
-- Data for Name: super; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.super (id_super, nome, descricao, status, rank, fraqueza, arqui_inimigo) FROM stdin;
\.


--
-- TOC entry 4917 (class 0 OID 16643)
-- Dependencies: 222
-- Data for Name: super_habilidade; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.super_habilidade (id_super, classe, poder) FROM stdin;
\.


--
-- TOC entry 4916 (class 0 OID 16628)
-- Dependencies: 221
-- Data for Name: super_tipo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.super_tipo (id_super, id_tipo) FROM stdin;
\.


--
-- TOC entry 4912 (class 0 OID 16587)
-- Dependencies: 217
-- Data for Name: tipo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo (id_tipo, nome, descricao) FROM stdin;
\.


--
-- TOC entry 4919 (class 0 OID 16667)
-- Dependencies: 224
-- Data for Name: vilao; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vilao (id_super_vilao, situacao) FROM stdin;
\.


--
-- TOC entry 4734 (class 2606 OID 16586)
-- Name: administrador administrador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_pkey PRIMARY KEY (id_adm);


--
-- TOC entry 4732 (class 2606 OID 16579)
-- Name: equipamento equipamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipamento
    ADD CONSTRAINT equipamento_pkey PRIMARY KEY (id_equipamento);


--
-- TOC entry 4748 (class 2606 OID 16661)
-- Name: heroi heroi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.heroi
    ADD CONSTRAINT heroi_pkey PRIMARY KEY (id_super_heroi);


--
-- TOC entry 4742 (class 2606 OID 16617)
-- Name: missao_equipamento missao_equipamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_equipamento
    ADD CONSTRAINT missao_equipamento_pkey PRIMARY KEY (id_missao, id_equipamento);


--
-- TOC entry 4752 (class 2606 OID 16683)
-- Name: missao_heroi missao_heroi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_heroi
    ADD CONSTRAINT missao_heroi_pkey PRIMARY KEY (id_super_heroi, id_missao);


--
-- TOC entry 4740 (class 2606 OID 16607)
-- Name: missao missao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao
    ADD CONSTRAINT missao_pkey PRIMARY KEY (id_missao);


--
-- TOC entry 4754 (class 2606 OID 16698)
-- Name: missao_vilao missao_vilao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_vilao
    ADD CONSTRAINT missao_vilao_pkey PRIMARY KEY (id_missao, id_super_vilao);


--
-- TOC entry 4746 (class 2606 OID 16649)
-- Name: super_habilidade super_habilidade_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_habilidade
    ADD CONSTRAINT super_habilidade_pkey PRIMARY KEY (id_super, classe, poder);


--
-- TOC entry 4738 (class 2606 OID 16600)
-- Name: super super_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super
    ADD CONSTRAINT super_pkey PRIMARY KEY (id_super);


--
-- TOC entry 4744 (class 2606 OID 16632)
-- Name: super_tipo super_tipo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_tipo
    ADD CONSTRAINT super_tipo_pkey PRIMARY KEY (id_super, id_tipo);


--
-- TOC entry 4736 (class 2606 OID 16593)
-- Name: tipo tipo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo
    ADD CONSTRAINT tipo_pkey PRIMARY KEY (id_tipo);


--
-- TOC entry 4750 (class 2606 OID 16673)
-- Name: vilao vilao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vilao
    ADD CONSTRAINT vilao_pkey PRIMARY KEY (id_super_vilao);


--
-- TOC entry 4761 (class 2606 OID 16662)
-- Name: heroi heroi_super_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.heroi
    ADD CONSTRAINT heroi_super_id_fk FOREIGN KEY (id_super_heroi) REFERENCES public.super(id_super);


--
-- TOC entry 4755 (class 2606 OID 16608)
-- Name: missao missao_adm_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao
    ADD CONSTRAINT missao_adm_id_fk FOREIGN KEY (id_adm) REFERENCES public.administrador(id_adm);


--
-- TOC entry 4756 (class 2606 OID 16623)
-- Name: missao_equipamento missao_eqp_eqp_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_equipamento
    ADD CONSTRAINT missao_eqp_eqp_id_fk FOREIGN KEY (id_equipamento) REFERENCES public.equipamento(id_equipamento);


--
-- TOC entry 4757 (class 2606 OID 16618)
-- Name: missao_equipamento missao_eqp_missao_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_equipamento
    ADD CONSTRAINT missao_eqp_missao_id_fk FOREIGN KEY (id_missao) REFERENCES public.missao(id_missao);


--
-- TOC entry 4763 (class 2606 OID 16684)
-- Name: missao_heroi missao_heroi_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_heroi
    ADD CONSTRAINT missao_heroi_id_fk FOREIGN KEY (id_super_heroi) REFERENCES public.heroi(id_super_heroi);


--
-- TOC entry 4764 (class 2606 OID 16689)
-- Name: missao_heroi missao_heroi_missao_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_heroi
    ADD CONSTRAINT missao_heroi_missao_id_fk FOREIGN KEY (id_missao) REFERENCES public.missao(id_missao);


--
-- TOC entry 4765 (class 2606 OID 16704)
-- Name: missao_vilao missao_vilao_missao_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_vilao
    ADD CONSTRAINT missao_vilao_missao_id_fk FOREIGN KEY (id_missao) REFERENCES public.missao(id_missao);


--
-- TOC entry 4766 (class 2606 OID 16699)
-- Name: missao_vilao missao_vilao_super_vilao_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_vilao
    ADD CONSTRAINT missao_vilao_super_vilao_id_fk FOREIGN KEY (id_super_vilao) REFERENCES public.vilao(id_super_vilao);


--
-- TOC entry 4760 (class 2606 OID 16650)
-- Name: super_habilidade super_habilidade_super_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_habilidade
    ADD CONSTRAINT super_habilidade_super_id_fk FOREIGN KEY (id_super) REFERENCES public.super(id_super);


--
-- TOC entry 4758 (class 2606 OID 16633)
-- Name: super_tipo super_tipo_super_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_tipo
    ADD CONSTRAINT super_tipo_super_id_fk FOREIGN KEY (id_super) REFERENCES public.super(id_super);


--
-- TOC entry 4759 (class 2606 OID 16638)
-- Name: super_tipo super_tipo_tipo_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_tipo
    ADD CONSTRAINT super_tipo_tipo_id_fk FOREIGN KEY (id_tipo) REFERENCES public.tipo(id_tipo);


--
-- TOC entry 4762 (class 2606 OID 16674)
-- Name: vilao vilao_super_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vilao
    ADD CONSTRAINT vilao_super_id_fk FOREIGN KEY (id_super_vilao) REFERENCES public.super(id_super);


-- Completed on 2024-08-20 16:55:20

--
-- PostgreSQL database dump complete
--

