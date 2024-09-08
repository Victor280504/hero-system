--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-09-08 20:14:22

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
-- TOC entry 215 (class 1259 OID 17505)
-- Name: administrador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.administrador (
    id_adm integer NOT NULL,
    nome character varying,
    contato character varying,
    login character varying,
    senha character varying,
    endereco character varying,
    data_inicio_adm date
);


ALTER TABLE public.administrador OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17510)
-- Name: administrador_id_adm_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.administrador_id_adm_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.administrador_id_adm_seq OWNER TO postgres;

--
-- TOC entry 4935 (class 0 OID 0)
-- Dependencies: 216
-- Name: administrador_id_adm_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.administrador_id_adm_seq OWNED BY public.administrador.id_adm;


--
-- TOC entry 217 (class 1259 OID 17511)
-- Name: equipamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipamento (
    id_equipamento integer NOT NULL,
    nome character varying,
    qtd_estoque integer,
    tipo character varying
);


ALTER TABLE public.equipamento OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 17516)
-- Name: equipamento_id_equipamento_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipamento_id_equipamento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipamento_id_equipamento_seq OWNER TO postgres;

--
-- TOC entry 4936 (class 0 OID 0)
-- Dependencies: 218
-- Name: equipamento_id_equipamento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipamento_id_equipamento_seq OWNED BY public.equipamento.id_equipamento;


--
-- TOC entry 219 (class 1259 OID 17517)
-- Name: heroi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.heroi (
    id_super_heroi bigint NOT NULL,
    disponibilidade character varying,
    contato character varying
);


ALTER TABLE public.heroi OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 17522)
-- Name: missao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao (
    id_missao integer NOT NULL,
    descricao character varying,
    data date,
    status character varying,
    local character varying,
    rank character varying,
    id_adm bigint NOT NULL
);


ALTER TABLE public.missao OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 17527)
-- Name: missao_equipamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao_equipamento (
    id_missao bigint NOT NULL,
    id_equipamento bigint NOT NULL,
    quantidade integer
);


ALTER TABLE public.missao_equipamento OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 17530)
-- Name: missao_heroi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao_heroi (
    id_super_heroi bigint NOT NULL,
    id_missao bigint NOT NULL
);


ALTER TABLE public.missao_heroi OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 17533)
-- Name: missao_id_missao_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.missao_id_missao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.missao_id_missao_seq OWNER TO postgres;

--
-- TOC entry 4937 (class 0 OID 0)
-- Dependencies: 223
-- Name: missao_id_missao_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.missao_id_missao_seq OWNED BY public.missao.id_missao;


--
-- TOC entry 224 (class 1259 OID 17534)
-- Name: missao_vilao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.missao_vilao (
    id_missao bigint NOT NULL,
    id_super_vilao bigint NOT NULL
);


ALTER TABLE public.missao_vilao OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 17537)
-- Name: super; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.super (
    id_super integer NOT NULL,
    nome character varying,
    descricao character varying,
    status character varying,
    rank character varying,
    fraqueza character varying,
    arqui_inimigo character varying
);


ALTER TABLE public.super OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 17542)
-- Name: super_habilidade; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.super_habilidade (
    id_super bigint NOT NULL,
    classe character varying NOT NULL,
    poder character varying NOT NULL
);


ALTER TABLE public.super_habilidade OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 17651)
-- Name: super_heroi; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.super_heroi AS
 SELECT s.id_super,
    s.nome,
    s.descricao,
    s.status,
    s.rank,
    s.fraqueza,
    s.arqui_inimigo,
    h.contato,
    h.disponibilidade
   FROM public.super s,
    public.heroi h
  WHERE (s.id_super = h.id_super_heroi);


ALTER VIEW public.super_heroi OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 17547)
-- Name: super_id_super_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.super_id_super_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.super_id_super_seq OWNER TO postgres;

--
-- TOC entry 4938 (class 0 OID 0)
-- Dependencies: 227
-- Name: super_id_super_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.super_id_super_seq OWNED BY public.super.id_super;


--
-- TOC entry 228 (class 1259 OID 17548)
-- Name: super_tipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.super_tipo (
    id_super bigint NOT NULL,
    id_tipo bigint NOT NULL
);


ALTER TABLE public.super_tipo OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 17557)
-- Name: vilao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vilao (
    id_super_vilao bigint NOT NULL,
    situacao character varying
);


ALTER TABLE public.vilao OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 17655)
-- Name: super_vilao; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.super_vilao AS
 SELECT s.id_super,
    s.nome,
    s.descricao,
    s.status,
    s.rank,
    s.fraqueza,
    s.arqui_inimigo,
    v.situacao
   FROM public.super s,
    public.vilao v
  WHERE (s.id_super = v.id_super_vilao);


ALTER VIEW public.super_vilao OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 17551)
-- Name: tipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo (
    id_tipo integer NOT NULL,
    nome character varying,
    descricao character varying
);


ALTER TABLE public.tipo OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 17556)
-- Name: tipo_id_tipo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_id_tipo_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tipo_id_tipo_seq OWNER TO postgres;

--
-- TOC entry 4939 (class 0 OID 0)
-- Dependencies: 230
-- Name: tipo_id_tipo_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_id_tipo_seq OWNED BY public.tipo.id_tipo;


--
-- TOC entry 4744 (class 2604 OID 17562)
-- Name: administrador id_adm; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrador ALTER COLUMN id_adm SET DEFAULT nextval('public.administrador_id_adm_seq'::regclass);


--
-- TOC entry 4745 (class 2604 OID 17563)
-- Name: equipamento id_equipamento; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipamento ALTER COLUMN id_equipamento SET DEFAULT nextval('public.equipamento_id_equipamento_seq'::regclass);


--
-- TOC entry 4746 (class 2604 OID 17564)
-- Name: missao id_missao; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao ALTER COLUMN id_missao SET DEFAULT nextval('public.missao_id_missao_seq'::regclass);


--
-- TOC entry 4747 (class 2604 OID 17565)
-- Name: super id_super; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super ALTER COLUMN id_super SET DEFAULT nextval('public.super_id_super_seq'::regclass);


--
-- TOC entry 4748 (class 2604 OID 17566)
-- Name: tipo id_tipo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo ALTER COLUMN id_tipo SET DEFAULT nextval('public.tipo_id_tipo_seq'::regclass);


--
-- TOC entry 4750 (class 2606 OID 17568)
-- Name: administrador administrador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_pkey PRIMARY KEY (id_adm);


--
-- TOC entry 4752 (class 2606 OID 17570)
-- Name: equipamento equipamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipamento
    ADD CONSTRAINT equipamento_pkey PRIMARY KEY (id_equipamento);


--
-- TOC entry 4754 (class 2606 OID 17572)
-- Name: heroi heroi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.heroi
    ADD CONSTRAINT heroi_pkey PRIMARY KEY (id_super_heroi);


--
-- TOC entry 4758 (class 2606 OID 17574)
-- Name: missao_equipamento missao_equipamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_equipamento
    ADD CONSTRAINT missao_equipamento_pkey PRIMARY KEY (id_missao, id_equipamento);


--
-- TOC entry 4760 (class 2606 OID 17576)
-- Name: missao_heroi missao_heroi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_heroi
    ADD CONSTRAINT missao_heroi_pkey PRIMARY KEY (id_super_heroi, id_missao);


--
-- TOC entry 4756 (class 2606 OID 17578)
-- Name: missao missao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao
    ADD CONSTRAINT missao_pkey PRIMARY KEY (id_missao);


--
-- TOC entry 4762 (class 2606 OID 17580)
-- Name: missao_vilao missao_vilao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_vilao
    ADD CONSTRAINT missao_vilao_pkey PRIMARY KEY (id_missao, id_super_vilao);


--
-- TOC entry 4766 (class 2606 OID 17582)
-- Name: super_habilidade super_habilidade_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_habilidade
    ADD CONSTRAINT super_habilidade_pkey PRIMARY KEY (id_super, classe, poder);


--
-- TOC entry 4764 (class 2606 OID 17584)
-- Name: super super_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super
    ADD CONSTRAINT super_pkey PRIMARY KEY (id_super);


--
-- TOC entry 4768 (class 2606 OID 17586)
-- Name: super_tipo super_tipo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_tipo
    ADD CONSTRAINT super_tipo_pkey PRIMARY KEY (id_super, id_tipo);


--
-- TOC entry 4770 (class 2606 OID 17588)
-- Name: tipo tipo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo
    ADD CONSTRAINT tipo_pkey PRIMARY KEY (id_tipo);


--
-- TOC entry 4772 (class 2606 OID 17590)
-- Name: vilao vilao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vilao
    ADD CONSTRAINT vilao_pkey PRIMARY KEY (id_super_vilao);


--
-- TOC entry 4773 (class 2606 OID 17591)
-- Name: heroi heroi_super_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.heroi
    ADD CONSTRAINT heroi_super_id_fk FOREIGN KEY (id_super_heroi) REFERENCES public.super(id_super) ON DELETE CASCADE;


--
-- TOC entry 4774 (class 2606 OID 17596)
-- Name: missao missao_adm_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao
    ADD CONSTRAINT missao_adm_id_fk FOREIGN KEY (id_adm) REFERENCES public.administrador(id_adm) ON DELETE SET NULL;


--
-- TOC entry 4775 (class 2606 OID 17601)
-- Name: missao_equipamento missao_eqp_eqp_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_equipamento
    ADD CONSTRAINT missao_eqp_eqp_id_fk FOREIGN KEY (id_equipamento) REFERENCES public.equipamento(id_equipamento) ON DELETE CASCADE;


--
-- TOC entry 4776 (class 2606 OID 17606)
-- Name: missao_equipamento missao_eqp_missao_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_equipamento
    ADD CONSTRAINT missao_eqp_missao_id_fk FOREIGN KEY (id_missao) REFERENCES public.missao(id_missao) ON DELETE CASCADE;


--
-- TOC entry 4777 (class 2606 OID 17611)
-- Name: missao_heroi missao_heroi_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_heroi
    ADD CONSTRAINT missao_heroi_id_fk FOREIGN KEY (id_super_heroi) REFERENCES public.heroi(id_super_heroi) ON DELETE CASCADE;


--
-- TOC entry 4778 (class 2606 OID 17616)
-- Name: missao_heroi missao_heroi_missao_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_heroi
    ADD CONSTRAINT missao_heroi_missao_id_fk FOREIGN KEY (id_missao) REFERENCES public.missao(id_missao) ON DELETE CASCADE;


--
-- TOC entry 4779 (class 2606 OID 17621)
-- Name: missao_vilao missao_vilao_missao_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_vilao
    ADD CONSTRAINT missao_vilao_missao_id_fk FOREIGN KEY (id_missao) REFERENCES public.missao(id_missao) ON DELETE CASCADE;


--
-- TOC entry 4780 (class 2606 OID 17626)
-- Name: missao_vilao missao_vilao_super_vilao_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.missao_vilao
    ADD CONSTRAINT missao_vilao_super_vilao_id_fk FOREIGN KEY (id_super_vilao) REFERENCES public.vilao(id_super_vilao) ON DELETE CASCADE;


--
-- TOC entry 4781 (class 2606 OID 17631)
-- Name: super_habilidade super_habilidade_super_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_habilidade
    ADD CONSTRAINT super_habilidade_super_id_fk FOREIGN KEY (id_super) REFERENCES public.super(id_super) ON DELETE CASCADE;


--
-- TOC entry 4782 (class 2606 OID 17636)
-- Name: super_tipo super_tipo_super_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_tipo
    ADD CONSTRAINT super_tipo_super_id_fk FOREIGN KEY (id_super) REFERENCES public.super(id_super) ON DELETE CASCADE;


--
-- TOC entry 4783 (class 2606 OID 17641)
-- Name: super_tipo super_tipo_tipo_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.super_tipo
    ADD CONSTRAINT super_tipo_tipo_id_fk FOREIGN KEY (id_tipo) REFERENCES public.tipo(id_tipo) ON DELETE CASCADE;


--
-- TOC entry 4784 (class 2606 OID 17646)
-- Name: vilao vilao_super_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vilao
    ADD CONSTRAINT vilao_super_id_fk FOREIGN KEY (id_super_vilao) REFERENCES public.super(id_super) ON DELETE CASCADE;


-- Completed on 2024-09-08 20:14:22

--
-- PostgreSQL database dump complete
--

